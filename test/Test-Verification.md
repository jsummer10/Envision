# Test Verification

## Unit Tests

### How To Run Unit Tests

```
$ python3 run.py -t
```

### Test 1: World Output

Verify that a world file is created in the worlds directory

### Test 2: Input Parser (txt)

Verify that txt input files are read and parsed in correctly

### Test 3: Input Parser (ini)

Verify that ini input files are read and parsed in correctly

### Test 4: Thorough 

End-to-end testing of a single Envision run

### Test 5: Run Gazebo

Verify that running Envision with the ```-o``` argument opens the world file in Gazebo after running Envision

## Current Test Results

<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
</head>
<body>
    <div class="row">
        <div class="col-xs-12 col-sm-10 col-md-10">
            <table class='table table-hover table-responsive'>
                <thead>
                    <tr>
                        <th>__main__.EnvisionTests</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class='success'>
                        <td class="col-xs-10">test 1 - World Output</td>
                        <td class="col-xs-1">
                            <span class="label label-success" style="display:block;width:40px;">Pass</span>
                    </tr>
                    <tr class='success'>
                        <td class="col-xs-10">test 2 - Input Parser (txt)</td>
                        <td class="col-xs-1">
                            <span class="label label-success" style="display:block;width:40px;">Pass</span>
                        </td>
                    </tr>
                    <tr class='success'>
                        <td class="col-xs-10">test 3 - Input Parser (ini)</td>
                        <td class="col-xs-1">
                            <span class="label label-success" style="display:block;width:40px;">Pass</span>
                        </td>
                    </tr>
                    <tr class='success'>
                        <td class="col-xs-10">test 4 - Thorough</td>
                        <td class="col-xs-1">
                            <span class="label label-success" style="display:block;width:40px;">Pass</span>
                    </tr>
                    <tr class='success'>
                        <td class="col-xs-10">test 5 - Run Gazebo</td>
                        <td class="col-xs-1">
                            <span class="label label-success" style="display:block;width:40px;">Pass</span>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>