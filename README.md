# A dummy Renku activity annotation plugin

This repository contains an dummy activity annotation plugin for Renku. It simply extends adds to each renku activity
with a very simple, static annotation.

After forking this repository make sure that you fill out the following fields:
 * `setup.py`
	- author
	- author_email
	- name
	- description
	- entry_points: this defines the entry point for a activity annotation plugin.
	  Make sure that it points to the correct module and function name.
