var a = document.getElementById('togglePassword');
var p = document.getElementById('password');


a.addEventListener('click', function (e) {
   const type = p.getAttribute('type') === 'password' ? 'text' : 'password';
   p.setAttribute('type', type);
   this.classList.toggle('fa-eye-slash');
});



