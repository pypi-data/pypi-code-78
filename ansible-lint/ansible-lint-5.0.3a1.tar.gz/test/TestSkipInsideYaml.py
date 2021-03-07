import pytest

ROLE_TASKS = '''\
---
- name: test command-instead-of-module
  command: git log
  changed_when: false
- name: test command-instead-of-module (skipped)
  command: git log  # noqa command-instead-of-module
  changed_when: false
'''

ROLE_TASKS_WITH_BLOCK = '''\
---
- name: bad git 1  # noqa git-latest
  action: git a=b c=d
- name: bad git 2
  action: git a=b c=d
- name: Block with rescue and always section
  block:
    - name: bad git 3  # noqa git-latest
      action: git a=b c=d
    - name: bad git 4
      action: git a=b c=d
  rescue:
    - name: bad git 5  # noqa git-latest
      action: git a=b c=d
    - name: bad git 6
      action: git a=b c=d
  always:
    - name: bad git 7  # noqa git-latest
      action: git a=b c=d
    - name: bad git 8
      action: git a=b c=d
'''

PLAYBOOK = '''\
- hosts: all
  tasks:
    - name: test hg-latest
      action: hg
    - name: test hg-latest (skipped)  # noqa hg-latest
      action: hg

    - name: test git-latest and partial-become
      become_user: alice
      action: git
    - name: test git-latest and partial-become (skipped)  # noqa git-latest partial-become
      become_user: alice
      action: git

    - name: test YAML and var-spacing
      get_url:
        url: http://example.com/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/file.conf
        dest: "{{dest_proj_path}}/foo.conf"
    - name: test YAML and var-spacing (skipped)
      get_url:
        url: http://example.com/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/really_long_path/file.conf  # noqa yaml
        dest: "{{dest_proj_path}}/foo.conf"  # noqa var-spacing

    - name: test deprecated-command-syntax
      command: creates=B chmod 644 A
    - name: test deprecated-command-syntax
      command: warn=yes creates=B chmod 644 A
    - name: test deprecated-command-syntax (skipped via no warn)
      command: warn=no creates=B chmod 644 A
    - name: test deprecated-command-syntax (skipped via skip_ansible_lint)
      command: creates=B chmod 644 A
      tags:
        - skip_ansible_lint
'''

ROLE_META = '''\
galaxy_info:  # noqa meta-no-info
  author: your name  # noqa meta-incorrect
  description: missing min_ansible_version and platforms. author default not changed
  license: MIT
'''

ROLE_TASKS_WITH_BLOCK_BECOME = '''\
- hosts: localhost
  tasks:
    - name: foo
      become: true
      block:
        - name: bar
          become_user: jonhdaa
          command: "/etc/test.sh"
'''


def test_role_tasks(default_text_runner):
    results = default_text_runner.run_role_tasks_main(ROLE_TASKS)
    assert len(results) == 1


def test_role_tasks_with_block(default_text_runner):
    results = default_text_runner.run_role_tasks_main(ROLE_TASKS_WITH_BLOCK)
    assert len(results) == 4


@pytest.mark.parametrize(
    ('playbook_src', 'results_num'),
    (
        (PLAYBOOK, 7),
        (ROLE_TASKS_WITH_BLOCK_BECOME, 0),
    ),
    ids=('generic', 'with block become inheritance'),
)
def test_playbook(default_text_runner, playbook_src, results_num):
    results = default_text_runner.run_playbook(playbook_src)
    assert len(results) == results_num


def test_role_meta(default_text_runner):
    results = default_text_runner.run_role_meta_main(ROLE_META)
    assert len(results) == 0
