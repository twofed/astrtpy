function getdata(extentable) {
    var exten = priority = app = appdata = all = [];
    // //var priority= [];
    // var app = [];
    // var appdata= [];
    // var all =[];
        for(var i = 1; i < extentable.length; i++){
            var result = extentable[i];
            exten[i] = result.exten;
            priority[i] = result.priority;
            app[i] = result.app;
            appdata[i]=result.appdata;
            all[i] =result;
            document.write('exten => ' +result.exten + ','+ result.priority + ','+result.app+'('+result.appdata+')<br>')
        }
        // console.log(exten);
        // console.log(priority);
        // console.log(app);
        // console.log(appdata);
        // console.log(extentable[1]);
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

function drawtable(extentable) {
    extentable.splice(0,1);
// var editor = new $('#tableext').dataTable.Editor( {} );
//


$('#tableext').DataTable( {
    // ajax: '/api/staff',
    // dom: 'Bfrtip',
    select: {items: 'cells',
             info: false},
    data:  extentable,

    columns: [
        { data: 'id',name: 'id',title:'id',class: "id", visible:"false"},
        { data: 'context',name: 'context',title:'Context',class: "edit context" },
        { data: 'exten' ,name: 'exten' ,title:'Exten',class: "edit exten"},
        { data: 'priority' ,name: 'priority' ,title:'Priority',class: "edit priority"},
        { data: 'app' ,name: 'app' ,title:'App',class: "edit app"},
        { data: 'appdata' ,name: 'appdata' ,title:'Appdata',class: "edit appdata"},
        { data: 'lastmoddate' ,name: 'lastmoddate' ,title:'Lastmoddate',class: "noedit"}
    ]
    // , buttons: [
    //     { extend: 'create', editor: editor },
    //     { extend: 'edit',   editor: editor },
    //     { extend: 'remove', editor: editor }
    // ]
} );

var table = $('#tableext').DataTable();
var cell = null;



$(document).on('click', 'td.edit', function() {
    if ($('.ajax').length!=0){
         return false}
    $('.ajax').html($('.ajax input').val());
    $('.ajax').removeClass('ajax');
    $(this).addClass('ajax');
    $(this).html('<input id="editbox" size="' + $(this).text().length + '" value="' + $(this).text() + '" type="text">');
    $('#editbox').focus();
    cell = table.row( this ).data();
});
$(document).on('keydown', 'td.edit', function (event){
    arr = $(this).attr('class').split( " " );
    // if(cell[arr[1]]==$('.ajax input').val()){
    //          return false
    //      }
    if(event.which == 13)
    {   console.log(cell[arr[1]]+'________'+$('.ajax input').val());
        var table = $('table').attr('id');
        function ajsend() {
            if (cell[arr[1]]!=$('.ajax input').val()){
            $.ajax({ type: "POST",
            url:"/updateexten/",
            data: "value="+$('.ajax input').val()+"&id="+cell['id']+"&field="+arr[1]+"&table="+table})
        }else{return false}}
        ajsend();
        $('.ajax').html($('.ajax input').val());
        $('.ajax').removeClass('ajax');
    }
});

$(document).on('blur', '#editbox', function(){
    $('.ajax').html($('.ajax input').val());
    $('.ajax').removeClass('ajax');
//     var arr = $('td.edit').attr('class').split( " " );
//     //console.log(arr);
//     var table = $('table').attr('id');
//     $.ajax({ type: "POST",
//         url:"/updateexten/",
//         data: "value="+$('.ajax input').val()+"&id="+cell['id']+"&field="+arr[2]+"&table="+table,
//         success: function(data){
//             //console.log(cell[arr[2]]+'________'+$('.ajax input').val());
//
//         }});
 });


}