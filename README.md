# SPELL CHECKER
An attempt to impliment spell checker using raw python

## To use in project user QueryChecker Fxn
check [example.py](./src/example.py) for more detail.



## Installation
1. Create virtual env (proj_env) and install requirements
``` bash
source proj_env/bin/activate
(proj_env) $ pip3 install -r requirements.txt
```

2. Run command
```bash
(proj_env) $ cd src
(proj_env) $ python3 manage.py run
```

## Details
- [Complete Detail](./res/README.md)



## Sample output

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
http://norvig.com/spell-correct.html
