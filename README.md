# Python Boilerplate
> Lightweight boilerplate for small python projects
> Comes with easy-to-configure sqlite db and basic CRUD methods
> Boilerplate follows PEP8 standard

## Startup
    Create virtualenv
    pip install -r requirements.txt
    git init  &&  git add .  &&  git commit -m "initial"
    git remote add origin {GITREPO.git}
    git branch -M main
    git push origin main
    python main.py

## Features

## Composition
    | assets
    | modules
        db.py
        utils.py
        | tests
            test_db.py
            test_utils.py
    .editorconfig
    .gitignore
    config.example.ini
    main.py
    requirements.txt
    
- assets:
- modules:
- tests
- config
- main py

## Tests
```sh
pytest (run all tests)
pytest modules/tests/test_db.py (run separate testcase)
pytest -v -m slow (run only decorated tag-mark: @pytest.mark.slow)
pytest -v -m "not slow" (inverse - exclude tests decorated with 'slow')
pytest -s (show print messages)
```
