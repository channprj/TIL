"""Post Revision Plugin for Pelican.

This plugin read the Git commit hitory for each article or page file, and store
the history as a meta data to the article or page object, so that templates can
make use of this information to show post revision history.

When this plugin is installed, the ``article`` and ``page`` object has an extra
meta data named ``history``, which is a list of ``<date, msg>`` tuples in
reverse order by date.
"""
import subprocess
import dateutil

from pelican import signals


def generate_post_revision(generator):
  project_root = generator.settings.get('PROJECT_ROOT', None)
  github_url = generator.settings.get('GITHUB_URL', None)
  if github_url is not None and github_url.endswith('/'):
    github_url = github_url.rstrip('/')

  pages = []
  pages += getattr(generator, 'articles', [])
  pages += getattr(generator, 'pages', [])
  for page in pages:
    path = getattr(page, 'source_path', None)
    if path is None:
      continue
    try:
      output = subprocess.check_output('git log --format="%%ai|%%s" %s'\
          % (path), shell=True)
      commits = []
      for line in output.split('\n'):
        line = line.strip()
        if len(line) == 0:
          continue
        parts = line.split('|')
        date, msg = dateutil.parser.parse(parts[0]), '|'.join(parts[1:])
        commits.append((date, msg))
      setattr(page, 'history', commits)

      if github_url is None or project_root is None:
        continue

      relative_path = path.replace(project_root, '')
      if relative_path.startswith('/'):
        relative_path = relative_path.lstrip('/')

      setattr(page, 'github_history_url', '%s/commits/master/%s' %\
          (github_url, relative_path))
    except:
      continue


def register():
  signals.article_generator_finalized.connect(generate_post_revision)
  signals.page_generator_finalized.connect(generate_post_revision)
