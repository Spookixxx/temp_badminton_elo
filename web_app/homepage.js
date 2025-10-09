// This script should run after the HTML content has been fully loaded.
document.addEventListener('DOMContentLoaded', () => {
    
    // Find all the image containers on the page.
    const containers = document.querySelectorAll('.image-container');

    // Loop through each container to apply the layout logic.
    containers.forEach(container => {
        // Get all the direct children (the images) of the current container.
        const items = container.children;
        const itemCount = items.length;

        // Check for the specific condition: 
        // 1. There is an ODD number of items (itemCount % 2 !== 0).
        // 2. There is MORE than 1 item (itemCount > 1).
        if (itemCount > 1 && itemCount % 2 !== 0) {
            
            // If the condition is met, find the index of the middle item.
            // For an array of 5 items (indices 0,1,2,3,4), Math.floor(5 / 2) gives us 2, which is the correct middle index.
            const middleIndex = Math.floor(itemCount / 2);

            // Add the special 'center-item' class to the identified middle element.
            // This class uses the CSS 'order' property to visually place it in the center.
            items[middleIndex].classList.add('center-item');
        }
    });
});
