$(document).ready(function(){
    // blog view start
    $.ajax({
        url:'/api/userBlogView/',
        method:"GET",
        success:function(data){
            var html = "";
            $.each(data,function(i,item){
                html +='<tr>'+
                '<td hidden="true">'+item.id+'</td>'+
                '<td hidden="true">'+item.auther+'</td>'+
                '<td>'+item.title+'</td>'+
                '<td>'+item.content+'</td>'+
                // '<td>'+item.images+'</td>'+
                '<td>'+item.publication_date+'</td>'+
                '<td><a href="/api/blogEdit/'+item.id+'/ "class="btn btn-primary update" id='+item.id+' data-toggle="modal" data-target="#educationadd" >Edit</a> <a href="edu_edit/'+item.id+'/ "class="btn btn-danger delete" data-toggle="modal" id='+item.id+' data-target="#deleteeducation">Delete</a></td>'+
                '</tr>';
            });
            $('#blogview').html(html);
        }
    })
    // blog view end
    $('#blog').on('submit',function(e){
        serializeData = $('#blog :input').serializeArray();
        console.log(serializeData);
        myurl="/api/userBlogPost/";
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
});