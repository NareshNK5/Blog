$(document).ready(function(){
    $('#user').on('click',function(e){
        // serializeData = $('#user :input').serializeArray();
        // e.preventDefault();
        var serializeData = new FormData(this);
        console.log(serializeData);
        console.log(serializeData);
        myurl="/api/registerUserSave/";
        $.ajax({
            data : serializeData,
            url : myurl,
            type : 'POST',
            // dataType : 'json',
            contentType: false,
            processData: false,
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
});