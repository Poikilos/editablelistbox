# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [git] - 2022-08-04
(Poikilos)
### Changed
(editablelistbox)
- Use PEP8 more.
  - Fix spacing.
  - Rename variables.
- Do not use builtin list as a variable name (change to items).
- Rename ind to index (O brother...lets not save 2 characters, lets make
  it readable instead.)
- Document init params.
- Rename placeListBoxEditable to placeLabels

(example-minimal)
- Use PEP8 more.
  - Fix spacing.
  - Rename variables.
  - Change the module name.
- Reduce comments.
  - Make variables self-explanatory (and follow PEP8 regarding word
    order) such as:
    change `column_frame ...  # Column frame` to `column_frame ...`
