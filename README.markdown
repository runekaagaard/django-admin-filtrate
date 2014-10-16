## About ##
This Django app makes it easier to create custom filters in the change list of
Django Admin and supplies a `TreeFilter` and a `DateRangeFilter` too. Se below.

Tested on Django 1.2.3 and from @15ea9a9 1.3.1.

## Updating to 1.4-1.7 support ##

There are no release yet, but a version tested with 1.4 and 1.7 can be installed with pip like:

    pip install git+git://github.com/runekaagaard/django-admin-filtrate@19f56144bfff2180cdc4e3f89770d7423c2b0318

I still need to test it with 1.5 and 1.6, update the documentation and then coax PyPi into making a release. Help could be great :)
Major differences in this version is:

- `lookup_allowed()` no longer needed.
- Uses the new builtin Django Filter classes.
- No need to register with `filtrate.register_filter`.

## Installation

Stub.

## Usage

Stub.
