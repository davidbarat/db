# import module snippets
import sys
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes, to_native

def main():

    module = AnsibleModule(
        argument_spec=dict(
            text=dict(),
        ),
    )

    text = module.params['text']

    text="plop " + text +" plop"

    changed = False

    result = dict(
        changed=changed,
        text=text
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
