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
Enter your string: simr adr peopel

<table>
    <tr>
        <th>Word</th><th>isCorrect</th><th>possibleWord</th><th>suggestList</th>
    </tr>
    <tr>
        <th>simr</th><th>False</th><th>six</th><th>['six', 'sri', 'air', 'sit', 'sirs', 'sir'] </th>
    </tr>
    <tr>
        <th>adr</th><th>False</th><th>and</th><th>['and', 'or', 'do', 'r', 'mr', 'di', 'pair', 'air', 'de', 'adds', 'd', 'aim', 'da', 'ur', 'sir', 'dr', 'hair', 'add']</th>
    </tr>
    <tr>
        <th>peopel</th><th>False</th><th>people</th><th>['people']</th>
    </tr>
</table>

## References
- ref 1
- ref 1
- ref 1
- ref 1
- ref 1
