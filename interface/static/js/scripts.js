


function deleteDataButton(btn){
    var currentRow = $(btn).closest("tr");
    var data = $('#jobs_table').DataTable().row(currentRow).data();
    var id = data['_id'];
    var string = data['role'] + " at " + data['company'] + " on " + data['date'];

//    Update confirm popup body text with selected job application
    $('#delete_modal_body_id').val(id);
    $('#delete_modal_body_text').val(string);
}


function deleteDataConfirmButton(){
    var id = $('#delete_modal_body_id').val();

    $.ajax({
        url: '/delete_selected_data/'+id,
        success: function(response) {
            $('#alert_message_table_update').html('<div class="alert alert-danger">Your '
            +'job application has been successfully deleted'
            +'.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>')
            cancelModifyButton();
          },
          error: function(xhr) {
            //Do Something to handle error
            alert("error: "+xhr);
         }
    });
}



function modifyDataButton(btn){
    var row = $(btn).closest("tr");

//    Show columns 1,8,9 (Cancel, save, delete buttons)
    $('#jobs_table').DataTable().columns( [1,8,9] ).visible( true );

//    Hide all irrelevant row buttons
    $('#jobs_table').find('.cancel-data button').addClass('d-none');
    row.find('.cancel-data button').removeClass('d-none');
    $('#jobs_table').find('.save-data button').addClass('d-none');
    row.find('.save-data button').removeClass('d-none');
    $('#jobs_table').find('.delete-data button').addClass('d-none');
    row.find('.delete-data button').removeClass('d-none');

//      TODO: If value is 'null' then forcefully change to input field instead of button
//    Add inputs for changing values
    var idx = 0;
    var rowLength = 8; // (Cancel-btn, Role, Company, Date, Website, Status, Save-btn, Delete-btn)
    row.find('td').each(function(){

        if(idx > 1 && idx < rowLength-1){
            var oldValue = this.innerHTML;
            // TODO: Add custom input fields to each value inputs
            if (idx == 4){ // IF DATE
                this.innerHTML = '<button class="btn btn-link" onclick="editValueInput(this)" name="date">'+oldValue+'</button>'
            }
            else if (idx == 6){ // IF STATUS
                this.innerHTML = '<select class="custom-select" name="website"> <option value="waiting for reply">waiting for reply</option>'
                +'<option value="interview">interview</option> <option value="accepted">accepted</option>'
                +'<option value="rejection">rejected</option> </select>';
            }
            else{
                this.innerHTML = '<button class="btn btn-link" onclick="editValueInput(this)" name="text">'+oldValue+'</button>'
            }
        }
        idx++;
    })


//    Disable table movement whilst in edit mode
    $('#jobs_table_paginate').prop( "hidden", true );
    $('#jobs_table_length select').prop( "disabled", true );
    $('#jobs_table_filter input').prop('disabled', true);
    //    TODO: NEEDS TABLE HEADER DISABLE (Clicking on header whilst modifying japp messed it up)


//    Hide columns 1 (Modify button)
    $('#jobs_table').DataTable().columns( [0] ).visible( false );
    row.find('td').css('background-color', 'grey');
}

function cancelModifyButton(){
//    Show columns
    $('#jobs_table').DataTable().columns( [0] ).visible( true );

//    Remove disable table movement
    $('#jobs_table_paginate').prop( "hidden", false );
    $('#jobs_table_length select').prop( "disabled", false );
    $('#jobs_table_filter input').prop('disabled', false);
    //    TODO: NEEDS TABLE HEADER ENABLE

//    Un-highlight row background
//    $(btn).closest("tr").find('td').removeAttr("style");
//    Hide Columns
    $('#jobs_table').DataTable().columns( [1,8,9] ).visible( false );

//    Reload table
    $('#jobs_table').DataTable().ajax.reload();
}

function editValueInput(btn){
    var oldValue = btn.innerHTML;
    var inputType = btn.name;
    var parentNode = btn.parentNode;

    if (inputType == "date"){
        parentNode.innerHTML = '<input type="date" placeholder="'+oldValue+'">';
    }
    else{ // inputType == text
        parentNode.innerHTML = '<input type="text" placeholder="'+oldValue+'">';
    }
    // Button is replaced with a different input field

    //Enable save button if edit clicked
//    var saveBtn = $(parentNode).closest("tr").find('.save-data button');
//    if (saveBtn.is(':disabled')){
//        saveBtn.prop('disabled', false);
//    }

    // Focus on input when clicked
    parentNode.firstElementChild.focus();

}

function saveDataButton(btn){
    alert("Saving changes...");
    var currentRow = $(btn).closest("tr");
    var data = $('#jobs_table').DataTable().row(currentRow).data();
    var id = data['_id'];

    var rowLength = 5;
    var idx = 0;
            // Atm only 5 data columns (Role, Company, Date, Website, Status)
            // Is +6 because skipping first column in later loop

    var listNewValues = new Array(rowLength);
    var allInputs = $(btn).closest("tr").find('td :input'); // Input includes buttons
//    TODO: Try and find a way to eliminate buttons as input
    allInputs.each( function(){
        if(idx > 0 && idx < rowLength+1){ // Ignore first Cancel-btn column
            var value = '';

            if (this.value.replace(/\s+/g, '') != "") { // Button been clicked and not empty
                value = this.value;
            }
            else if (this.innerHTML != "") { // Button has not been clicked (not edited)
                value = this.innerHTML;
            }
            else { // Button been clicked but empty input field
                value = this.placeholder;
                // TODO: Require them to fill in empty field
            }
            listNewValues[idx-1] = value;
        }
        idx++;
    })

    alert(listNewValues);


//    Ajax call to update database
    $.ajax({
        url: '/update_selected_data/'+id+'/'+listNewValues,
        success: function(response) {
            $('#alert_message_table_update').html('<div class="alert alert-success">Your '
            +'changes has been successfully saved'
            +'.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>')
            cancelModifyButton();
          },
          error: function(xhr) {
            //Do Something to handle error
            alert("error: "+xhr);
         }
    });

    alert("Fin");
}




// SAVE job applications page
function checkEnableOther(select_box){

    if (select_box.value == 'other'){
        $('#website_dropdown_other_text').removeClass('d-none');
        $('#website_dropdown_other_text').prop( "disabled", false );
    }
    else{
        $('#website_dropdown_other_text').addClass('d-none');
        $('#website_dropdown_other_text').prop( "disabled", true );
    }

}