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
                '<td><img class="w-75" src='+item.images+' alt="" /></td>'+
                '<td>'+item.publication_date+'</td>'+
                '<td><a href="/api/blogEdit/'+item.id+'/ "class="btn btn-primary update" id='+item.id+' data-toggle="modal" data-target="#blogadd" >Edit</a> <a href="edu_edit/'+item.id+'/ "class="btn btn-danger delete" data-toggle="modal" id='+item.id+' data-target="#deleteblog">Delete</a></td>'+
                '</tr>';
            });
            $('#blogview').html(html);
        }
    })
    // blog view end
    $('#blog').on('submit',function(e){
        serializeData = $('#blog :input').serializeArray();
        let id = $("#Myid").attr("value");
        console.log(id);
        console.log(serializeData);
        myurl="/api/userBlogPost/"+id+"/";
        console.log(myurl);
        $.ajax({
            data : serializeData,
            url : myurl,
            type : 'POST',
            dataType : 'json',
            success:function(data){
                alert(data);
                location.reload();
            },
            error:function(data){
                alert(data);
                location.reload();

            }
        });
    });

    // blog view end
    $("#blogview").on('click','.update',function(e){
        e.preventDefault();
        var id=$(this).attr('id');
        console.log("id",id);
        $("input[id=Myid]").val(id);
        var myurl=$(this).attr('href');
        console.log("url",myurl);

        $("#title").change(function(){
            $('input[name=title]').val($(this).val())
        })

        $("#content").change(function(){
            $('textarea[name=content]').val($(this).val())
        })
        $.ajax({
            method : 'GET',
            url : myurl,
            dataType : "json",
            success:function(data){
                $('input[name=id]').val(data.id);
                $('input[name=title]').val(data.title);
                $('textarea[name=content]').val(data.content);
            }
        })
    })
// blog view end

// blog get delete start
$('#blogview').on('click','.delete',function(e){
    e.preventDefault();
    var myurl = $(this).attr('href');
    console.log(myurl);
    $.ajax({
        url : myurl,
        method : 'GET',
        async : true,
        success:function(data){
            $('input[id=Myid]').val(data.id);
            $('input[name=course]').val(data.course);

        }
    })
})
// blog get delete end

// deleteblog start
$('#deleteblog').on('click','.delete',function(){
    id  = $("#Myid").attr('value');
    console.log(id);
    myurl = 'edu_delete/'+id+'/';
    console.log(myurl);
    $.ajax({
        url : myurl,
        method:'DELETE',
        success:function(data){
            alert("Deleted");
            location.reload();
        }
    })
})
//deleteblog end
});