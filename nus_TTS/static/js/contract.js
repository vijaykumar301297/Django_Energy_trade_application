const gasBtn = document.querySelector('.btn_gas');
const elecBtn = document.querySelector('.btn_elec');
const mwhbtn = document.querySelector('.unit');
const fixedBtn = document.querySelector('.btn_fixed');
const indexBtn = document.querySelector('.btn_index');
const indexshow = document.querySelector('.indexed');
const price = document.querySelector('.commodity_input');

const commodityblock = document.querySelector('.calendar_block');
const total  = document.querySelector('.Consumption_input').value;


const gas = function () {
    mwhbtn.style.display ='block';
    gasBtn.classList.add('active');
    elecBtn.classList.remove('active');
    elecBtn.style.background = '#DFE6ED';
    elecBtn.style.border = 'none';
};

const ele = function () {
    mwhbtn.style.display ='none';
    elecBtn.classList.add('active');
    gasBtn.classList.remove('active');
    gasBtn.style.background = '#DFE6ED';
    gasBtn.style.border = 'none';
};

const fixed = function () {
    document.querySelector('.fi').innerHTML ="Term, Consumption and Price - Fixed Price Contract";
    const h2 = document.querySelector(".calendar_block");
    let html = `<div class="commodity_price_block" >
                            <label for="" class="commodity_label">Commodity Price (per MWh)</label>
                            <input type="text" placeholder="0.00" class="commodity_input">
                        </div>`;
    h2.insertAdjacentHTML("afterend", html);
    indexshow.style.display ='none';
    fixedBtn.classList.add('active');
    indexBtn.classList.remove('active');
    indexBtn.style.background = '#DFE6ED';
    document.querySelector('.commodity_price_block').style.display ='block';
    indexBtn.style.border = 'none';
    document.querySelector('#remove').remove();
};


const index = function() {

    indexshow.style.display ='block';
    indexBtn.classList.add('active');
    fixedBtn.classList.remove('active');
    fixedBtn.style.background = '#DFE6ED';
    fixedBtn.style.border = 'none';
    document.querySelector('.commodity_price_block').remove();
    document.querySelector('.fi').innerHTML ="Term and Consumption - Indexed Contract";
    showindexdiv();
};

gasBtn.addEventListener('click', gas);

elecBtn.addEventListener('click', ele);

fixedBtn.addEventListener('click', fixed);

indexBtn.addEventListener('click', index);



// for(var i =0; i<dropdown_click; i++) {
//     allowable.addEventListener('click', function() {
//         var dropdown_click = document.querySelector('.clicks_heading');
//         // dropdown_click.addEventListener('change', function() {

//         // });

//     });

// }

document.addEventListener('DOMContentLoaded', function(){
    var clicked = document.querySelector('input[type = "checkbox"]');
    clicked.addEventListener('change', function(){
        if (clicked.checked) {
            document.querySelector('.divide_block').style.display='block';
        }
        else {
            document.querySelector('.divide_block').style.display='none';
        }
    });
});

// Form

var curTab = 0;
showTab(curTab);


function showTab(n) {
    // console.log(n);
    var x = document.getElementsByClassName('tab');
    // console.log(x);
    x[n].style.display ='block';

    if (n==0) {
        document.getElementById('prevBtn').style.display ='none';
    }
    else {
        document.getElementById('prevBtn').style.display ='inline';
    }

    if (n == (x.length -1)) {
        document.getElementById('nextBtn').style.innerHTML = 'Create Contract';
    }
    else {
        document.getElementById('nextBtn').style.innerHTML = 'next';
    }
    fixStepIndicator(n)
}

function nextPrev(n) {

    var x = document.getElementsByClassName('tab');

    if (n==1 && !validateForm()) return false;

    x[curTab].style.display = "none";
    curTab = curTab + n;

    if (curTab>= x.length) {
        document.getElementById('createContract').submit();
        return false
    }
    showTab(curTab);
}

function validateForm() {

    var x, y, i, valid = true;

    x = document.getElementsByClassName('tab');

    y =x[curTab].getElementsByTagName('input');

    for(i =0; i<y.length; i++) {
        // console.log(y[i]);
        if (y[i].value == "") {
            y[i].className += " invalid";
            valid = false;
        }
    }
    if (valid) {
      document.getElementsByClassName("step")[curTab].className += " finish";
    }
    return valid;
}

function fixStepIndicator(n) {
    // console.log(n);
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
      x[i].className = x[i].className.replace(" active", "");
    }

    x[n].className += " active";
}

function showindexdiv() {
    const divindex = document.querySelector("#contractterm");
    let a =  `<div class="tab" id="remove">
                <div class="main">
                    <div class="heading_secondary--block">
                        <h2 class="secondary_heading--main">
                            Index Details
                        </h2>
                    </div>
                    <div class="inside_block">
                        <div class="structure_block">
                            <div class="cons_pow">
                                <div class="label1">
                                    <label for="" class="index_type">Index Structure Type</label>
                                </div>
                                <div class="cons_pow_span">
                                    <span class="btn btn_consum" value="Consumption">
                                        Consumption (MWH)
                                    </span>
                                    <span class="btn btn_power" value="Power">
                                        Power(MW)
                                    </span>
                                </div>
                            </div>
                            <div class="allowable_trade_block">
                                <div class="trade_name">
                                    <h4 class="Allowable_trade--heading">
                                        Allowable trade periods
                                    </h4>
                                </div>
                                <div class="allow_span_clivk">
                                    <span class="allow_click">
                                        +  Add allowable trade period
                                    </span>
                                </div>
                            </div>
                            <div class="trade_add_block">
                                <div class="consumption_click">
                                    <div class="calendar-yearly">
                                        <div class="calendar_yearly">
                                            <div class="select_val">
                                                <select name="" id="" class="clicks_heading">
                                                    <option value="Calendar Yearly">Calendar Yearly</option>
                                                    <option value="Calendar Quarterly">Calendar Quarterly</option>
                                                    <option value="Calendar Monthly">Calendar Monthly</option>
                                                </select>
                                            </div>

                                            <div class="input_clicks">
                                                <label for="" class="clicks_secondary_heading">Clicks / tranches</label>
                                                <input type="number" class="clicks_entry">
                                            </div>
                                            <div class="del">
                                                <span><i class="material-icons">delete</i></span>
                                            </div>
                                        </div>
                                        <div class="checkbox">
                                            <span class="consum_per"><input type="checkbox" name="" id="consum_per" > % Consumption</span>
                                            <span class="consum_mwh"><input type="checkbox" name="" id="consum_mwh" > #MWhs</span>
                                        </div>
                                    </div>
                                    <div class="calendar-Quarterly" style="display: none;">
                                        <div class="calendar_Quarterly">
                                            <div class="select_val">
                                                <select name="" id="" class="clicks_heading">
                                                    <option value="Calendar Yearly">Calendar Yearly</option>
                                                    <option value="Calendar Quarterly">Calendar Quarterly</option>
                                                    <option value="Calendar Monthly">Calendar Monthly</option>
                                                </select>
                                            </div>

                                            <div class="input_clicks">
                                                <label for="" class="clicks_secondary_heading">Clicks / tranches</label>
                                                <input type="number" class="clicks_entry">
                                            </div>
                                            <div class="del">
                                                <span><i class="material-icons">delete</i></span>
                                            </div>
                                        </div>
                                        <div class="checkbox">
                                            <span class="consum_per"><input type="checkbox" name="" id="consum_per" > % Consumption</span>
                                            <span class="consum_mwh"><input type="checkbox" name="" id="consum_mwh" > #MWhs</span>
                                        </div>
                                    </div>
                                    <div class="calendar-Monthly" style="display: none;">
                                        <div class="calendar_Monthly">
                                            <div class="select_val">
                                                <select name="" id="" class="clicks_heading">
                                                    <option value="Calendar Yearly">Calendar Yearly</option>
                                                    <option value="Calendar Quarterly">Calendar Quarterly</option>
                                                    <option value="Calendar Monthly">Calendar Monthly</option>
                                                </select>
                                            </div>

                                            <div class="input_clicks">
                                                <label for="" class="clicks_secondary_heading">Clicks / tranches</label>
                                                <input type="number" class="clicks_entry">
                                            </div>
                                            <div class="del">
                                                <span><i class="material-icons">delete</i></span>
                                            </div>
                                        </div>
                                        <div class="checkbox">
                                            <span class="consum_per"><input type="checkbox" name="" id="consum_per" > % Consumption</span>
                                            <span class="consum_mwh"><input type="checkbox" name="" id="consum_mwh" > #MWhs</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="postion_block">
                            <div class="label1">
                                <label for="" class="index">Open Position pricing mechanism</label>
                            </div>
                            <div class="">
                                <select name="" id="" class="select_price_mechanism">
                                    <option value="">Please Select Pricing Mechanism</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;

    divindex.insertAdjacentHTML("afterend", a);
    const allowable = document.querySelector('.allow_click');
    allowable.addEventListener('click', function() {
        console.log('click');
        document.querySelector('.trade_add_block').style.display= 'block';
    });

    var del = document.querySelector('.material-icons');
    del.addEventListener('click', function() {
        var delind = document.querySelector('.trade_add_block');
        delind.remove(delind.selectedIndex);
    });

    // var count  = document.querySelector('.clicks_heading').options.length;
    // console.log(count);

};

const allowable = document.querySelector('.allow_click');
allowable.addEventListener('click', function() {
    console.log('click');
    document.querySelector('.trade_add_block').style.display= 'block';
});

var del = document.querySelector('.material-icons');
del.addEventListener('click', function() {
    var delind = document.querySelector('.trade_add_block');
    delind.remove(delind.selectedIndex);
});


var datepicker = new ej.calendars.DatePicker({
    placeholder: 'Choose a from date',
    focus: function(){
        datepicker.show();
    }
});
datepicker.appendTo('#element');

var datepicker = new ej.calendars.DatePicker({
    placeholder: 'Choose a to date',
    focus: function(){
        datepicker.show();
    }
});
datepicker.appendTo('#element');