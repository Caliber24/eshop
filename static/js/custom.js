// console.log('this is custom.js')

function sendArticleComment(articleId) {
    // console.log('submit article comment');
    let comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    // let parent = $('#commentText').val();
    // console.log(comment);
    $.get('/articles/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        // console.log(res);
        // document.getElementById('body').scrollIntoView();
        // location.reload();
        $('#comments_area').html(res);
        $('#parent_id').val('');
        $('#commentText').val('');
        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comment_box' + parentId).scrollIntoView({behavior: 'smooth'});

        } else {
            document.getElementById('comments_area').scrollIntoView({behavior: 'smooth'});
        }

    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    // window.scrollTo()
    document.getElementById('comment_form').scrollIntoView({behavior: 'smooth'});
}

function filterProducts() {
    const filterPrice = $('#sl2').val();
    const startPrice = filterPrice.split(',')[0];
    const endPrice = filterPrice.split(',')[1];
    $('#start_price').val(startPrice);
    $('#end_price').val(endPrice);
    $('#filter_form').submit();
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}

function showLargeImage(imageSrc) {
    console.log(imageSrc);
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image_modal').attr('href', imageSrc);

}

function addProductToOrder(productId) {
    // console.log(productId);
    const productCount = $('#product_count').val();
    $.get('/order/add-to-order?product_id=' + productId + "&count=" + productCount).then(res => {

        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed && res.status === 'no_auth') {
                window.location.href = '/login';
            }

        });
        // console.log(res);
        //     if (res.status === 'success') {
        //         Swal.fire({
        //             title: "اعلان",
        //             text: "",
        //             icon: "success",
        //             showCancelButton: false,
        //             confirmButtonColor: "#3085d6",
        //             cancelButtonColor: "#d33",
        //             confirmButtonText: "باشه ممنون"
        //         });
        //     } else if (res.status === "not found") {
        //         Swal.fire({
        //             title: "اعلان",
        //             text: "محصول مورد نظر یافت نشد",
        //             icon: "error",
        //             showCancelButton: false,
        //             confirmButtonColor: "#3085d6",
        //             confirmButtonText: "باشه ممنون"
        //         });
        //
        //     }
        //
        // });
    });
}


function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


//detailId = order detailId
//state => increase decrease
function changeOrderDetailCount(detailId, state) {
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


//    ajax => asynchronous javascript and xml
//    json => java script object notation