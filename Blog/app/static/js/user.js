$(document).ready(function(){
    $('#user').on('click',function(e){
        serializeData = $('#user :input').serializeArray();
        console.log(serializeData);
        myurl="/api/registerUserSave/";
        $.ajax({
            data : serializeData,
            url : myurl,
            type : 'POST',
            dataType : 'json',
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

});