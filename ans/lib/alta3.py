#!/usr/bin/python3
"""Custom module for Transunion | rzfeeser@alta3.com"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'alta3'
}

DOCUMENTATION = """
---
My documentation goes here

- name: My custom module
  transunion:
    name: Russell Zachary Feeser
    new: True

"""

from ansible.module_utils.basic import AnsibleModule

def run_module():
    ## define what params users can pass as arguments
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_name='',
        new_name=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_name'] = module.params['name']
    result['new_name'] = module.params['name'] + " is an Alta3 employee!"

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'FAILME':
        module.fail_json(msg="You requested this module to fail", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
