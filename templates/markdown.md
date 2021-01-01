{{ name.firstname }} {{ name.surname }}
===========
- {{ location }}
- {{ email }}
{% for link in links %}
- [{{ link.text }}]({{ link.url }})
{% endfor %}

> {{ statement }}

Technical Skills
----------------

<table>
  <thead>
    <tr>
      <th></th>
      <th>Most experience</th>
      <th>Some experience</th>
      <th>Dabbled</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Languages</strong></td>
      <td>{{ skills.languages.most_experience|join(', ') }}</td>
      <td>{{ skills.languages.some_experience|join(', ') }}</td>
      <td>{{ skills.languages.dabbled|join(', ') }}</td>
    </tr>
    <tr>
      <td><strong>Frameworks and libraries</strong></td>
      <td>{{ skills.frameworks.most_experience|join(', ') }}</td>
      <td>{{ skills.frameworks.some_experience|join(', ') }}</td>
      <td>{{ skills.frameworks.dabbled|join(', ') }}</td>
    </tr>
    {% if skills.databases %}
      <td><strong>Databases, caches, message brokers etc.</strong></td>
      <td>{{ skills.databases.most_experience|join(', ') }}</td>
      <td>{{ skills.databases.some_experience|join(', ') }}</td>
      <td>{{ skills.databases.dabbled|join(', ') }}</td>
    {% endif %}
    <tr>
      <td><strong>Other</strong></td>
      <td colspan="3">{{ skills.other.values() | concat | join(', ') }}</td>
    </tr>
  </tbody>
</table>

Work Experience
---------------

{% for job in work_experience %}
- {{ job.start }} – {{ job.end }}: **{{ job.title }}**, *{{ job.company }}*
  {% if job.description is defined %}
    {% for bullet in job.description %}
    + {{ bullet|trim }}
    {% endfor %}
  {% endif %}
{% endfor %}

Side Projects
------------------

{% for pr in project_experience %}
- {{ pr.completed }}: **{{ pr.title }}**, [{{ pr.link.text }}]({{ pr.link.url }})
  {% if pr.description is defined %}
    {% for bullet in pr.description %}
    + {{ bullet|trim }}
    {% endfor %}
  {% endif %}
{% endfor %}

Certifications and Professional Development
------------------------

{% for cs in certifications %}- {{ cs.started }}{% if cs.completed is not equalto cs.started %}
 – {{ cs.completed }}{% endif %}: **{{ cs.title }}**, *{{ cs.provider }}*{% if cs.link is defined %}, [{{ cs.link.text }}]({{ cs.link.url }}){% endif %}

  {% if cs.modules is defined %}
    {% for mod in cs.modules %}
  + {{ mod.title }}, [{{ mod.link.text }}]({{ mod.link.url }})
    {% endfor %}
  {% endif %}
{% endfor %}

Education
---------
{% for ed in education %}
- {{ ed.start }} – {{ ed.end }}: **{{ ed.degree }}**, *{{ ed.university }}*{% if ed.grade is defined %}, {{ ed.grade }}{% endif %}

{% endfor %}