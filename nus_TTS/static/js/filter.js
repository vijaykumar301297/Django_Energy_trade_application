function myFunction() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (var i = 1; i < tr.length; i++) {
    var tds = tr[i].getElementsByTagName("td");
    var flag = false;
    for(var j = 0; j < tds.length; j++){
      var td = tds[j];
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        flag = true;
      }
    }
    if(flag){
        tr[i].style.display = "";
    }
    else {
        tr[i].style.display = "none";
    }
  }
}

const roleValue = document.querySelector('#role');
console.log(roleValue);
roleValue.addEventListener('change', function(e) {
    if(e.target.value ==='Parent') {
        document.querySelector('.select_parent--block').style.display='block';
        document.querySelector('.select_client--block').style.display='none';
       document.getElementById("p1").removeAttribute('disabled', 'false');
        document.querySelector('#parent_data').setAttribute('disabled','true');
    }
   else if(e.target.value==='Client') {
       document.querySelector('.select_client--block').style.display='block';
       document.querySelector('.select_parent--block').style.display='none';
        document.getElementById("parent_data").removeAttribute('disabled', 'false');
        document.getElementById("clients").removeAttribute('disabled', 'false');
       document.querySelector('#p1').setAttribute('disabled','true');
//       document.querySelector('.select_client--block').removeAttribute("disabled");
   }
   else {
       document.querySelector('.select_client--block').style.display='none';
       document.querySelector('.select_parent--block').style.display='none';

   }
});

$('select[multiple]').multiselect({
columns: 4,
placeholder: 'Select options'
});

//$(document).ready(function(){
//
//     var multipleCancelButton = new Choices('#clients', {
//        removeItemButton: true,
//        maxItemCount:5,
//        searchResultLimit:5,
//        renderChoiceLimit:5
//      });
//
//
// });


//	$('#clients').multiSelect();



//$("#clients").chosen({
//  no_results_text: "Oops, nothing found!"
//})
//const btnhome = document.querySelector('.')