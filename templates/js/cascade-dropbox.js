function cascade_dropbox(eleId){
  var warp = $('#'+eleId);
  var data = null;
  $.ajax({
    url: 'templates/js/DistrictData.xml',
    type: 'post',
    dataType: 'xml',
    success:function(result){
      data = result;
      var provinces = $(data).find('province');
      for(var i=0;i<provinces.length;i++){
        var newOption = $('<option>'+provinces.eq(i).attr('name')+'</option>')
        warp.find('.province').append(newOption);
      }
    }
  }).done(function() {
    var pcc = null;
    warp.find('.province').on('change',  function(event) {
      /* Act on the event */
      pcc = new PCC(this.value)
      warp.find('.city').html('<option>--请选择--</option>')
      warp.find('.country').html('<option>--请选择--</option>')
      if(pcc.province == '--请选择--'){
        $('#show').find('input').val('');
        return false;
      }
      for(var i=0;i<pcc.city.length;i++){
        var newOption = $('<option>'+pcc.city.eq(i).attr('name')+'</option>')
        warp.find('.city').append(newOption);
      }
      event.preventDefault();
    });
    warp.find('.city').on('change',  function(event) {
      /* Act on the event */
      warp.find('.country').html('<option>--请选择--</option>')
      if(warp.find('.city').val() == '--请选择--') return false;
      var countries = pcc.getCountriesByCity(warp.find('.city').val());
      for(var i=0;i<countries.length;i++){
        var newOption = $('<option>'+countries.eq(i).attr('name')+'</option>')
        warp.find('.country').append(newOption);
      }
      event.preventDefault();
    });
    warp.find('.country').on('change',function(event){
      var pro = warp.find('.province').val();
      var city = warp.find('.city').val();
      $('#show').find('input').val(pro+'-'+city+'-'+this.value) 
      event.preventDefault();
    });
  })
  function PCC(province){
    this.province = province;
    this.city = $(data).find('province[name='+this.province+']').find('city');
  }
  PCC.prototype.getCountriesByCity= function(city){
    return $(data).find('province[name='+this.province+']').find('city[name='+city+']').find('country');
  }
}