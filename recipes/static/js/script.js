// Example JavaScript code
document.addEventListener('DOMContentLoaded', function() {
    console.log("Page loaded!");

    // Function to open the modal with recipe details
    window.getRecipeDetails = function(recipeId) {
        $.ajax({
            url: '/get-recipe-details/' + recipeId,
            success: function(data) {
                $('#modalTitle').text(data.title);
                $('#modalSteps').html(data.instructions); // Adjust based on actual API response
                $('#recipeModal').show();
            }
        });
    }

    // Get the modal
    var modal = document.getElementById("recipeModal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});


