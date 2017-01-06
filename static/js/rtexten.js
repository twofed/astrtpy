function getdata(extentable) {
    var exten = [];
    var priority= [];
    var app = [];
    var appdata= [];
    var all =[];
        for(var i = 1; i < extentable.length; i++){
            var result = extentable[i];
            exten[i] = result.exten;
            priority[i] = result.priority;
            app[i] = result.app;
            appdata[i]=result.appdata;
            all[i] =result;
            document.write('exten => ' +result.exten + ','+ result.priority + ','+result.app+'('+result.appdata+')' +'\n\n' )
        }
        console.log(exten);
        console.log(priority);
        console.log(app);
        console.log(appdata);
        console.log(all);

        // var table = document.createElement('table');
        // table.border='4px double black';
        // var i=0;
        // for (r=1; r<exten.length; r++) {
        //     var row = table.insertRow(-1);
        //     if (exten[r]!=exten[r+1])
        //     {
        //      row.innerHTML = exten[r]
        //     }
        //     else {
        //         i++;
        //         row.rowSpan = i;
        //     }
        // }
        // document.getElementById('exten').appendChild(table);
    }

function check_exten(){
        if (extentable=='array') {
            alert('Ничего не найдено');
            return false
        }
        var exten = new Array();
        for(var i = 1; i< extentable.length; i++){
            exten[i] = extentable[i].exten;
        }
        for(var i=1; i<exten.length;i++){
            if(exten[i]==exten[i+1]){
                if (extentable[i].priority == extentable[i+1].priority && extentable[i].priority!='n'){
                    return alert('Найдены 2 контекста с одинаковым приоритетом и он не n! Приоритет 1 :' + extentable[i].priority
                        +' Приоритет 2:' +extentable[i+1].priority + 'Направление 1 :'+extentable[i].exten+' Направление 2 :'+extentable[i+1].exten )}
                return false;}
            else {
                return (i);
            }
            }
    }
