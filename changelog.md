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
    - Rename `placeListBoxEditable` to `gridAll`
    - Rename `saveEntryValue` to `_stopEntry` (It doesn't save to
      storage, only to the `Label`).
    - Rename `changeToEntry` to `_startEntry`.
    - Rename `up` to `_onUp` and `down` to `_onDown`
    - Rename `changeBackground` to `_onClick`
    - Rename `frameMaster` to `parent`
    - Rename ind to index (O brother...lets not save 2 characters, lets make
      it readable instead.)
    - and more
  - Document init params, and move other documentation comments to
    docstrings as well.
- Do not use builtin list as a variable name (change to items).

(example-minimal)
- Use PEP8 more.
  - Fix spacing.
  - Rename variables.
  - Change the module name.
- Reduce comments.
  - Make variables self-explanatory (and follow PEP8 regarding word
    order) such as:
    change `column_frame ...  # Column frame` to `column_frame ...`
  - Remove "Create the variable", "Constructor", "Get the name of the
    label", "Name", etc.  We get it ;)

### Fixed
- Preserve the label value when changing to an entry.
- Import rather than redefine globals that relate to unifying the look.
