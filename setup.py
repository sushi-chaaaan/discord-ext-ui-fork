from setuptools import setup
import re

version = ''
with open('discord/ext/ui/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(name='discord-ext-ui',
      author='sizumita',
      url='https://github.com/sizumita/discord-ext-ui',
      version=version,
      packages=['discord.ext.ui'],
      license='MIT',
      description='An Declarative UI Kit for discord.py',
      install_requires=['discord.py>=2.0.0'],
      python_requires='>=3.8.2'
      )