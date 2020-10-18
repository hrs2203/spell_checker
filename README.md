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
python3 manage.py run
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
        <td>simr</td><td>False</td><td>six</td><td>['six', 'sri', 'air', 'sit', 'sirs', 'sir'] </td>
    </tr>
    <tr>
        <td>adr</td><td>False</td><td>and</td><td>['and', 'or', 'do', 'r', 'mr', 'di', 'pair', 'air', 'de', 'adds', 'd', 'aim', 'da', 'ur', 'sir', 'dr', 'hair', 'add']</td>
    </tr>
    <tr>
        <td>peopel</td><td>False</td><td>people</td><td>['people']</td>
    </tr>
</table>

## References
- ref 1
- ref 1
- ref 1
- ref 1
- ref 1
