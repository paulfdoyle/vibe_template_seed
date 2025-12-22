# Project Template

Use this folder as a starting point for new project docs.

## How to use
1) Copy `projects/_template/` to `projects/<project>/`.
2) Rename files that include placeholders:
   - `project_summary_template.md` -> `project_summary_<project>.md`
   - `phases/phase01/actions/project_phase01_stage_foundation_action.md` -> `<project>_phase01_stage_foundation_action.md`
3) Replace placeholder text such as `<project>`, `<phase_name>`, and `<stage_name>`.
4) Update `support/docs/projectplan.md` to register the new project.
5) Run `python3 support/scripts/render_docs.py` to refresh formatted docs.

## Alternative
Run the initializer script instead of copying manually:
```
python3 support/scripts/init_project.py --project <project> --prefix <PREFIX> --owner "Name"
```
