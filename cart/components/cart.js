function updateCart() {
    $.ajax({
        url: '',  // URL to your Django view for updating the cart
        type: 'POST',  // Or 'GET' depending on your implementation
        data: {
            'total_products' // Include data to update the cart (e.g., product ID and quantity)
        },
        success: function(response) {
            // Update the cart total in the DOM
            $('total_products').text(response.total_products);
        },
        error: function(xhr, textStatus, errorThrown) {
            // Handle errors if necessary
        }
    });
}

// Add event listeners to cart modification actions
$('.btn-primary').click(function() {
    console.log('Button clicked');
    updateCart();
});



