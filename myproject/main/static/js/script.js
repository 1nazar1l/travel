const categoryList = document.getElementById('categoryList');
const countryCards = document.querySelectorAll('.country_card');

console.log(countryCards)

categoryList.addEventListener('click', (event) => {
    const selectedCategory = event.target.dataset.category;
    console.log(selectedCategory)

//     // Показываем/скрываем карточки в зависимости от выбранной категории
    countryCards.forEach((card) => {
        const cardCategories = card.dataset.categories.split(' ');
        // console.log(cardCategories)

        if (cardCategories.includes(selectedCategory) || selectedCategory === undefined) {
            card.classList.remove('hidden');
            console.log('True')
        } 
        else if (selectedCategory === 'remove' || selectedCategory === 'otmenit' ) {
            card.classList.remove('hidden');
        }
        else {
            card.classList.add('hidden');
        }
    });
});


function openToursPage(name) {
    // Формируем URL страницы игры
    let gamePageUrl = `/tours/${name}`;
    
    // Перенаправляем пользователя на страницу игры
    window.location.href = gamePageUrl;
  }
console.log("Hello")