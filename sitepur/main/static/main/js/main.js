 const select = document.querySelector('#id_buying_type')
const orderMap = document.querySelector('.map')

var map;

DG.then(function () {
    map = DG.map('map', {
        center: [55.76, 37.64],
        zoom: 11
    });

    DG.marker([55.76, 37.64]).addTo(map).bindPopup('Магазин брендовых товаров');
});

select.addEventListener('change', (e) => {
    e.target.value !== 'self' ? orderMap.style.display = 'none' : orderMap.style.display = 'block'
})