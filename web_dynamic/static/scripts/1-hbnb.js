$(document).ready(function () {
  const selectedAmenities = {};
  $('input[type="checkbox"][data-id]').change(function () {
    const amenityId = $(this).data('id');
    const amenityName = $(this).data('name');

    if ($(this).is(':checked')) {
      selectedAmenities[amenityId] = amenityName;
    } else {
      delete selectedAmenities[amenityId];
    }
    updateAmenitiesList();
  });

  function updateAmenitiesList() {
    const amenitiesArray = Object.values(selectedAmenities);
    let amenitiesList = amenitiesArray.join(', ');
    if (amenitiesList.length > 31) {
      amenitiesList = amenitiesList.slice(0, 31) + '...';
    }

    $('.amenities h4').text(amenitiesList);
  }
});
