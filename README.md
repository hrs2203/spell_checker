# SPELL CHECKER
An attempt to impliment spell checker using raw python\

## Installation
1. install requirements
``` bash
pip3 install -r requirements.txt
```

2. run command
```bash
cd src
python3 manage.py runserver
```

## Theory and Approach


## sample output
(proj_env) $ python3 manage.py run

Enter your string: simr adr peopel

<table>
    <tr>
        <th>Word</th><th>isCorrect</th><th>possibleWord</th><th>suggestList</th>
    </tr>
    <tr>
        <tr>simr</tr><tr>False</tr><tr>six</tr><tr>['six', 'sri', 'air', 'sit', 'sirs', 'sir'] </tr>
    </tr>
    <tr>
        <tr>adr</tr><tr>False</tr><tr>and</tr><tr>['and', 'or', 'do', 'r', 'mr', 'di', 'pair', 'air', 'de', 'adds', 'd', 'aim', 'da', 'ur', 'sir', 'dr', 'hair', 'add']</tr>
    </tr>
    <tr>
        <tr>peopel</tr><tr>False</tr><tr>people</tr><tr>['people']</tr>
    </tr>
</table>

## References
- ref 1
- ref 1
- ref 1
- ref 1
- ref 1
