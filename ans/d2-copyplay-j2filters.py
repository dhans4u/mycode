---
- hosts: futurama
  name: Copying files
  gather_facts: yes
  tasks:

  - name: Write out to a file
    copy:
      dest: ~/{{ inventory_hostname }}.facts
      content: "{{ ansible_facts | to_nice_json }}"
    delegate_to: localhost

  - name: Copy a file
    copy:
      dest: ~/ship.config
      src: /home/student/mycode/ans/ship.config

  - name: Print a hello to the screen # ANSIBLE IS NOT FOR PRINTING TO THE SCREEN
    debug:
      msg: "Hello TransUnion! Thanks for the invite :)"

...
