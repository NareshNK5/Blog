$(document).ready(function(){
    $('#user').on('submit',function(e){
        serializeData = $('#user :input').serializeArray();
        console.log(serializeData);
        let id = $("#Myid").attr("value");
        console.log(id);
        myurl="/api/registerUserSave/"+id+"/";
        console.log(myurl);
        $.ajax({
            data : serializeData,
            url : myurl,
            type : 'POST',
            dataType : 'json',
            success:function(data){
                alert("Posted");
                console.log(data.data);
            },
            error:function(data){
                alert("Retry");
                console.log(data.data);
            }
        });
    });

// user edit

// $("#userEdit").on('click','.update',function(e){
//     e.preventDefault();
    // var id=$("#userEdit").attr('id');
    // console.log("id",id);
    // $("input[id=Myid]").val(id);
    var myurl='/api/userProfileGet/'
    console.log("url",myurl);

    $("#username").change(function(){
        $('input[name=username]').val($(this).val())
    })

    $("#password").change(function(){
        $('input[name=password]').val($(this).val())
    })

    $("#cpassword").change(function(){
        $('input[name=password]').val($(this).val())
    })

    $("#mailid").change(function(){
        $('input[name=mailid]').val($(this).val())
    })

    $("#contact_no").change(function(){
        $('input[name=contact_no]').val($(this).val())
    })

    $("#Myid").change(function(){
        $('input[name=Myid]').val($(this).val())
    })
    $.ajax({
        method : 'GET',
        url : myurl,
        dataType : "json",
        success:function(data){
            $('input[name=Myid]').val(data.id);
            $('input[name=username]').val(data.username);
            $('input[name=password]').val(data.password);
            $('input[name=cpassword]').val(data.password);
            $('input[name=mailid]').val(data.mailid);
            $('input[name=contact_no]').val(data.contact_no);
        }
    })
// })

// user edit end
});