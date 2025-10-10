document.addEventListener('DOMContentLoaded', () => {
    
    const containers = document.querySelectorAll('.image-container');

    containers.forEach(container => {
        const items = container.children;
        const itemCount = items.length;

        if (itemCount > 1 && itemCount % 2 !== 0) {
            const middleIndex = Math.floor(itemCount / 2);
            items[middleIndex].classList.add('center-item');
        }
    });
});
