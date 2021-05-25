$(function () {
    //获取本地存储数据，并且转换成对象
    var arr = [];
    window.localStorage.clear();
    function getData() {
        if (localStorage.tableList == undefined) {
            arr = [];
        } else {
            arr = JSON.parse(localStorage.tableList);
        }
        return arr;


    }
    function saveData(data){
    //  var data = getData();
    //  JSON.stringify(localStorage.tableList);
      localStorage.tableList = JSON.stringify(data);
    }

    //把数据存到本地存储，并且转换成字符串格式的JSON
    $("#save").on("click", function () {
        var data = getData();
        //  JSON.stringify(localStorage.tableList);
        localStorage.tableList = JSON.stringify(data);
        console.log(data);

        $.ajax({
            url: "/designer/createAssess",
            type: "POST",
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            success: function (msg) {
                // alert("save success")
            }
        })

        add();
    });

    //增加行方法
    function add() {
        $("tr:not(tr:first,tr:last)").remove();//每次增加行前删除前面的行，否则会重复增加

        var data = getData();
        $.each(data, function (i, v) {
            $("<tr>").attr("index", i).html("<td contenteditable='true' data-role='method'>" + v.method + "</td>" + "<td contenteditable='true' data-role='percent'>" + v.percent + "</td>" + "<td contenteditable='true' data-role='cilo'>" + v.cilo + "</td>"+"<td><button class='btn btn-danger btn-sm'>DELETE</button></td>").insertBefore("tr:last");
        })
        saveData(data);
    }

    //点击增加按钮事件
    $("#add").on("click", function () {
        var data = getData();
        data.push({"method": "", "percent": "","cilo": ""});
        saveData(data);
        add();
    })


    //删除行方法，事件委派，根据当前点击的按钮的行的索引值
    $('table').on('click', '.btn-danger', function () {
        var data = getData();
        var index = $(this).parent().parent().attr("index");
        data.splice(index, 1);
        saveData(data);
        add();
    })


    //可编辑效果 contenteditable='true'
    $('table').on('blur', '[contenteditable="true"]', function () {
        var data = getData();
        var index = $(this).parent().attr('index');
        var val = $(this).html();
        var attr = $(this).attr('data-role');
        data[index][attr] = val;
        saveData(data);

    })
    add()


})
