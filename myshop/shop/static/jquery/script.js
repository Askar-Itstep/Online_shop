$(document).ready(function () {

    cart_len = $('.hidden.cart_len').html()
    // console.log(cart_len)
    cart_sum = $('.hidden.cart_sum').html()

    // запись
    if(cart_len !== undefined){
        localStorage.setItem('cart_len' , cart_len )
        localStorage.setItem('cart_sum', cart_sum )
    }
    // чтение
    else {
        cart_sum = localStorage.getItem('cart_sum')
        // $('.visible.cart_sum').html(cart_sum)
        cart_len = localStorage.getItem('cart_len')
        // $('.visible.cart_len').html(cart_len)

        $('.cart a').html('Your cart: '+cart_len+' item, '+ cart_sum)

    }


})