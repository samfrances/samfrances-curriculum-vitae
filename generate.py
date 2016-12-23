#!/usr/bin/env python

import yaml
import os
import sys
import argparse
import importlib

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

# Command-line interface
parser = argparse.ArgumentParser(description='Generate CV from Yaml source')
parser.add_argument("--src",
                    "-s",
                    help="yaml file source",
                    default="sam-frances-curriculum-vitae.yml")
parser.add_argument("--processor",
                    "-p",
                    help="data processing filter applied to yaml data source before template rendering")
parser.add_argument("--template",
                    "-t",
                    help="template file",
                    default="templates/markdown.md")
parser.add_argument("--debug",
                    "-d,",
                    help="show full python tracebacks when errors occur",
                    action="store_true",
                    default=False)

args = parser.parse_args()

src = os.path.abspath(os.path.join(os.getcwd(), args.src))

# If no directory specified, assume base directory is template directory
template_arg = args.template
if not os.path.dirname(args.template):
    template_arg = os.path.join("templates", template_arg)

# Extract full path of template, directory, and filename
template_fullpath = os.path.abspath(os.path.join(os.getcwd(), template_arg))
template_dir = os.path.abspath(os.path.dirname(template_fullpath))
template_name = os.path.basename(template_fullpath)



# Set up jinja environments
jenv_latex = Environment(
    loader=FileSystemLoader(template_dir),
    extensions=['jinja2.ext.with_'],
    block_start_string="\BLOCK{",
    block_end_string="}",
    variable_start_string="\VAR{",
    variable_end_string="}",
    comment_start_string="\#{",
    comment_end_string="}",
    trim_blocks=True,
    lstrip_blocks=True
)

jenv_default = Environment(
    loader=FileSystemLoader(template_dir),
    extensions=['jinja2.ext.with_'],
    trim_blocks=True,
    lstrip_blocks=True
)
# filter for talking a sequence of sequences and returning the concatenation
# of those sequences
jenv_markdown.filters['concat'] = lambda sequences: reduce(lambda x, y: x+y, sequences)

# Choose jinja environment based on file extension
extension = os.path.splitext(template_name)[1]
if extension == ".tex":
    jenv = jenv_latex
else:
    jenv = jenv_default


# Read the yaml source
try:
    with open(src, "r") as stream:
        variables = next(yaml.load_all(stream))
except IOError as e:
    if not args.debug:
        sys.stderr.write("{}: {}\n".format(e.strerror, e.filename))
        exit(1)
    else:
        raise
except yaml.parser.ParserError:
    if not args.debug:
        sys.stderr.write("Invalid Yaml file\n")
        exit(1)
    else:
        raise

# pass it through any specified processor, to filter and otherwise
# process the data from the yaml source file
try:
    if args.processor:
        processor = importlib.import_module('processors.{}'.format(args.processor))
        variables = processor.process(variables)
except ImportError:
    if not args.debug:
        sys.stderr.write("Processor module not found")
        exit(1)
    else:
        raise


# Get template and render
try:
    template = jenv.get_template(template_name)
except TemplateNotFound as e:
    if not args.debug:
        sys.stderr.write("Template not found: {}\n".format(e.message))
        exit(1)
    else:
        raise

print template.render(**variables).encode('utf-8')
