def main(ctx):
  return [
    testing(ctx),
    changes(ctx),
    release(ctx),
    notify(ctx),
  ]

def testing(ctx):
  return {
    'kind': 'pipeline',
    'type': 'docker',
    'name': 'testing',
    'platform': {
      'os': 'linux',
      'arch': 'amd64',
    },
    'steps': [
      {
        'name': 'lint',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'environment': {
          'PY_COLORS': '1',
        },
        'commands': [
          'tox -e lint',
        ],
      },
      {
        'name': 'test',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'environment': {
          'PY_COLORS': '1',
        },
        'commands': [
          'tox -e py3',
        ],
      },
      {
        'name': 'build',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'environment': {
          'PY_COLORS': '1',
        },
        'command': [
          'tox -e build',
        ],
      },
      {
        'name': 'codacy',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'environment': {
          'PY_COLORS': '1',
          'CODACY_PROJECT_TOKEN': {
            'from_secret': 'codacy_token',
          },
        },
        'commands': [
          'tox -e codacy',
        ],
      },
    ],
    'trigger': {
      'ref': [
        'refs/heads/master',
        'refs/tags/**',
        'refs/pull/**',
      ],
    },
  }

def changes(ctx):
  return {
    'kind': 'pipeline',
    'type': 'docker',
    'name': 'changes',
    'platform': {
      'os': 'linux',
      'arch': 'amd64',
    },
    'clone': {
      'disable': True,
    },
    'steps': [
      {
        'name': 'clone',
        'image': 'plugins/git-action:1',
        'pull': 'always',
        'settings': {
          'actions': [
            'clone',
          ],
          'remote': 'https://github.com/%s' % (ctx.repo.slug),
          'branch': ctx.build.branch if ctx.build.event == 'pull_request' else 'master',
          'path': '/drone/src',
          'netrc_machine': 'github.com',
          'netrc_username': {
            'from_secret': 'github_username',
          },
          'netrc_password': {
            'from_secret': 'github_token',
          },
        },
      },
      {
        'name': 'generate',
        'image': 'toolhippie/calens:latest',
        'pull': 'always',
        'commands': [
          'calens >| CHANGELOG.md',
        ],
      },
      {
        'name': 'output',
        'image': 'toolhippie/calens:latest',
        'pull': 'always',
        'commands': [
          'cat CHANGELOG.md',
        ],
      },
      {
        'name': 'publish',
        'image': 'plugins/git-action:1',
        'pull': 'always',
        'settings': {
          'actions': [
            'commit',
            'push',
          ],
          'message': 'Automated changelog update [skip ci]',
          'branch': 'master',
          'author_email': 'kleister@webhippie.de',
          'author_name': 'Kleister',
          'netrc_machine': 'github.com',
          'netrc_username': {
            'from_secret': 'github_username',
          },
          'netrc_password': {
            'from_secret': 'github_token',
          },
        },
      },
    ],
    'depends_on': [
      'testing',
    ],
    'trigger': {
      'ref': [
        'refs/heads/master',
      ],
    },
  }

def release(ctx):
  return {
    'kind': 'pipeline',
    'type': 'docker',
    'name': 'release',
    'platform': {
      'os': 'linux',
      'arch': 'amd64',
    },
    'steps': [
      {
        'name': 'build',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'environment': {
          'PY_COLORS': '1',
        },
        'command': [
          'tox -e build',
        ],
      },
      {
        'name': 'release',
        'image': 'plugins/pypi:1',
        'pull': 'always',
        'settings': {
          'gemname': 'kleister',
          'gemspec': 'kleister.gemspec',
          'username': {
            'from_secret': 'pypi_username',
          },
          'password': {
            'from_secret': 'pypi_password',
          },
        },
      },
      {
        'name': 'checksum',
        'image': 'webhippie/python:latest',
        'pull': 'always',
        'commands': [
          'sha256sum dist/*.whl >| $(basename dist/*.whl .whl)',
          'sha256sum dist/*.tar.gz >| $(basename dist/*.tar.gz .tar.gz)',
        ],
      },
      {
        'name': 'gpgsign',
        'image': 'plugins/gpgsign:1',
        'pull': 'always',
        'settings': {
          'key': {
            'from_secret': 'gpgsign_key',
          },
          'passphrase': {
            'from_secret': 'gpgsign_passphrase',
          },
          'files': [
            'dist/*.whl',
            'dist/*.tar.gz',
          ],
          'detach_sign': True,
        },
      },
      {
        'name': 'changelog',
        'image': 'toolhippie/calens:latest',
        'pull': 'always',
        'commands': [
          'calens --version %s -o dist/CHANGELOG.md' % ctx.build.ref.replace("refs/tags/v", "").split("-")[0],
        ],
      },
      {
        'name': 'github',
        'image': 'plugins/github-release:1',
        'pull': 'always',
        'settings': {
          'api_key': {
            'from_secret': 'github_token',
          },
          'files': [
            'dist/*',
          ],
          'checksum': [
            'sha256',
          ],
          'title': ctx.build.ref.replace("refs/tags/", ""),
          'note': 'dist/CHANGELOG.md',
          'overwrite': True,
        },
      },
    ],
    'depends_on': [
      'testing',
    ],
    'trigger': {
      'ref': [
        'refs/tags/**',
      ],
    },
  }

def notify(ctx):
  return {
    'kind': 'pipeline',
    'type': 'docker',
    'name': 'notify',
    'platform': {
      'os': 'linux',
      'arch': 'amd64',
    },
    'clone': {
      'disable': True,
    },
    'steps': [
      {
        'name': 'execute',
        'image': 'plugins/matrix:1',
        'pull': 'always',
        'settings': {
          'username': {
            'from_secret': 'matrix_username',
          },
          'password': {
            'from_secret': 'matrix_password',
          },
          'roomid': {
            'from_secret': 'matrix_roomid',
          },
        },
      },
    ],
    'depends_on': [
      'testing',
      'changes',
      'release',
    ],
    'trigger': {
      'ref': [
        'refs/heads/master',
        'refs/tags/**',
      ],
      'status': [
        'failure',
      ],
    },
  }
