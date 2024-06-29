$(document).ready(function(){
    $('#user').on('submit',function(e){
        serializeData = $('#user :input').serializeArray();
        console.log(serializeData);
        myurl="/api/registerUserSave/";
        $.ajax({
            data : serializeData,
            url : myurl,
            type : 'POST',
            dataType : 'json',
            success:function(data){
                alert(data);
            },
            error:function(data){
                alert(data);
            }
        });
    });

    // $('#loginCheck').on('submit',function(){
    //     action="/api/loginCheck/" ;
    //     method="post";
    //     serializeData = $('#loginCheck :input').serializeArray();
    //     $.ajax({
    //         data:serializeData,
    //         type : method ,
    //         url : action,
    //         dataType : 'json',
    //         success:function(data){
    //             alert('login');
    //         },
    //         error:function(data){
    //             alert('not login');
    //         }

        // });
    // });
});