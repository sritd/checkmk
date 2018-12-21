// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// ails.  You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

// ----------------------------------------------------------------------------
// General functions for WATO
// ----------------------------------------------------------------------------

/* Used to check all checkboxes which have the given class set */
function wato_check_all(css_class) {
    var items = document.getElementsByClassName(css_class);

    // First check if all boxes are checked
    var all_checked = true, i;
    for(i = 0; i < items.length && all_checked == true; i++)
        if (items[i].checked == false)
            all_checked = false;

    // Now set the new state
    for(i = 0; i < items.length; i++)
        items[i].checked = !all_checked;
}

/* Make attributes visible or not when clicked on a checkbox */
function wato_toggle_attribute(oCheckbox, attrname) {
    var oEntry =   document.getElementById("attr_entry_" + attrname);
    var oDefault = document.getElementById("attr_default_" + attrname);

    // Permanent invisible attributes do
    // not have attr_entry / attr_default
    if (!oEntry){
        return;
    }

    if (oCheckbox.checked) {
        oEntry.style.display = "";
        oDefault.style.display = "none";
    }
    else {
        oEntry.style.display = "none";
        oDefault.style.display = "";
    }
}

/* Switch the visibility of all host attributes during the configuration
   of attributes of a host */
function wato_fix_visibility() {
    /* First collect the current selection of all host attributes.
       They are in the same table as we are */
    var current_tags = _get_effective_tags();
    if (!current_tags)
        return;

    var hide_topics = volatile_topics.slice(0);
    /* Now loop over all attributes that have conditions. Those are
       stored in the global variable wato_depends_on_tags, which is filled
       during the creation of the web page. */

    var index;
    for (var i = 0; i < wato_check_attributes.length; i++) {
        var attrname = wato_check_attributes[i];
        /* Now comes the tricky part: decide whether that attribute should
           be visible or not: */
        var display = "";

        // Always invisible
        if (hide_attributes.indexOf(attrname) > -1){
            display = "none";
        }

        // Visibility depends on roles
        if (display == "" && attrname in wato_depends_on_roles) {
            for (index = 0; index < wato_depends_on_roles[attrname].length; index++) {
                var role = wato_depends_on_roles[attrname][index];
                var negate = role[0] == "!";
                var rolename = negate ? role.substr(1) : role;
                var have_role = user_roles.indexOf(rolename) != -1;
                if (have_role == negate) {
                    display = "none";
                    break;
                }
            }
        }

        // Visibility depends on tags
        if (display == "" && attrname in wato_depends_on_tags) {
            for (index = 0; index < wato_depends_on_tags[attrname].length; index++) {
                var tag = wato_depends_on_tags[attrname][index];
                var negate_tag = tag[0] == "!";
                var tagname = negate_tag ? tag.substr(1) : tag;
                var have_tag = current_tags.indexOf(tagname) != -1;
                if (have_tag == negate_tag) {
                    display = "none";
                    break;
                }
            }
        }


        var oTr = document.getElementById("attr_" + attrname);
        if(oTr) {
            oTr.style.display = display;

            // Prepare current visibility information which is used
            // within the attribut validation in wato
            // Hidden attributes are not validated at all
            var oAttrDisp = document.getElementById("attr_display_" + attrname);
            if (!oAttrDisp) {
                oAttrDisp = document.createElement("input");
                oAttrDisp.name  = "attr_display_" + attrname;
                oAttrDisp.id  = "attr_display_" + attrname;
                oAttrDisp.type = "hidden";
                oAttrDisp.className = "text";
                oTr.appendChild(oAttrDisp);
            }
            if ( display == "none" ) {
                // Uncheck checkboxes of hidden fields
                var chkbox = oAttrDisp.parentNode.childNodes[0].childNodes[1].childNodes[0];
                chkbox.checked = false;
                wato_toggle_attribute(chkbox, attrname);

                oAttrDisp.value = "0";
            } else {
                oAttrDisp.value = "1";
            }

            // There is at least one item in this topic -> show it
            var topic = oTr.parentNode.childNodes[0].textContent;
            if (display == ""){
                index = hide_topics.indexOf(topic);
                if (index != -1)
                    delete hide_topics[index];
            }
        }
    }

    // FIXME: use generic identifier for each form
    var available_forms = [ "form_edit_host", "form_editfolder" ];
    for (var try_form = 0; try_form < available_forms.length; try_form++) {
        var my_form = document.getElementById(available_forms[try_form]);
        if (my_form != null) {
            for (var child in my_form.childNodes){
                oTr = my_form.childNodes[child];
                if (oTr.className == "nform"){
                    if( hide_topics.indexOf(oTr.childNodes[0].childNodes[0].textContent) > -1 )
                        oTr.style.display = "none";
                    else
                        oTr.style.display = "";
                }
            }
            break;
        }
    }
}

function _get_effective_tags()
{
    var current_tags = [];

    var container_ids = [ "wato_host_tags", "data_sources", "address" ];

    for (var a = 0; a < container_ids.length; a++) {
        var container_id = container_ids[a];

        var oHostTags = document.getElementById(container_id);

        if (!oHostTags)
            continue;

        var oTable = oHostTags.childNodes[0]; /* tbody */

        for (var i = 0; i < oTable.childNodes.length; i++) {
            var oTr = oTable.childNodes[i];
            var add_tag_id = null;
            if (oTr.tagName == "TR") {
                var oTdLegend = oTr.childNodes[0];
                if (oTdLegend.className != "legend") {
                    continue;
                }
                var oTdContent = oTr.childNodes[1];
                /* If the Checkbox is unchecked try to get a value from the inherited_tags */
                var oCheckbox = oTdLegend.getElementsByTagName("input")[0];
                if (oCheckbox.checked == false ){
                    var attrname = "attr_" + oCheckbox.name.replace(/.*_change_/, "");
                    if (attrname in inherited_tags && inherited_tags[attrname] !== null){
                        add_tag_id = inherited_tags[attrname];
                    }
                } else {
                    /* Find the <select>/<checkbox> object in this tr */
                    var elements = oTdContent.getElementsByTagName("input");
                    if (elements.length == 0)
                        elements = oTdContent.getElementsByTagName("select");

                    if (elements.length == 0)
                        continue;

                    var oElement = elements[0];
                    if (oElement.type == "checkbox" && oElement.checked) {
                        add_tag_id = oElement.name.substr(4);
                    } else if (oElement.tagName == "SELECT") {
                        add_tag_id = oElement.value;
                    }
                }
            }

            current_tags.push(add_tag_id);
            if (wato_aux_tags_by_tag[add_tag_id]) {
                current_tags = current_tags.concat(wato_aux_tags_by_tag[add_tag_id]);
            }
        }
    }
    return current_tags;
}


function wato_randomize_secret(id, len)
{
    var secret = "";
    for (var i=0; i<len; i++) {
        var c = parseInt(26 * Math.random() + 64);
        secret += String.fromCharCode(c);
    }
    var oInput = document.getElementById(id);
    oInput.value = secret;
}

function toggle_container(id)
{
    var obj = document.getElementById(id);
    if (has_class(obj, "hidden"))
        remove_class(obj, "hidden");
    else
        add_class(obj, "hidden");
}

function update_bulk_moveto(val) {
    var fields = document.getElementsByClassName("bulk_moveto");
    for(var i = 0; i < fields.length; i++)
        for(var a = 0; a < fields[i].options.length; a++)
            if(fields[i].options[a].value == val)
                fields[i].options[a].selected = true;
}

// .-Profile Repl----------------------------------------------------------.
// |          ____             __ _ _        ____            _             |
// |         |  _ \ _ __ ___  / _(_) | ___  |  _ \ ___ _ __ | |            |
// |         | |_) | '__/ _ \| |_| | |/ _ \ | |_) / _ \ '_ \| |            |
// |         |  __/| | | (_) |  _| | |  __/ |  _ <  __/ |_) | |            |
// |         |_|   |_|  \___/|_| |_|_|\___| |_| \_\___| .__/|_|            |
// |                                                  |_|                  |
// +-----------------------------------------------------------------------+

var profile_replication_progress = new Array();

function wato_do_profile_replication(siteid, est, progress_text) {
    call_ajax("wato_ajax_profile_repl.py", {
        response_handler : function (handler_data, response_json) {
            var response = JSON.parse(response_json);
            var success = response.result_code === 0;
            var msg = response.result;

            set_profile_replication_result(handler_data["site_id"], success, msg);
        },
        error_handler    : function (handler_data, status_code, error_msg) {
            set_profile_replication_result(handler_data["site_id"], false,
                "Failed to perform profile replication [" + status_code + "]: " + error_msg);
        },
        method           : "POST",
        post_data        : "request=" + encodeURIComponent(JSON.stringify({
            "site": siteid
        })),
        handler_data     : {
            "site_id": siteid
        },
        add_ajax_id      : false
    });

    profile_replication_progress[siteid] = 20; // 10 of 10 10ths
    setTimeout("profile_replication_step('"+siteid+"', "+est+", '"+progress_text+"');", est/20);
}

function profile_replication_set_status(siteid, image, text) {
    var oImg = document.getElementById("site-" + siteid).childNodes[0];
    oImg.title = text;
    oImg.src = "images/icon_"+image+".png";
}

function profile_replication_step(siteid, est, progress_text) {
    if (profile_replication_progress[siteid] > 0) {
        profile_replication_progress[siteid]--;
        var perc = (20.0 - profile_replication_progress[siteid]) * 100 / 20;
        var img;
        if (perc >= 75)
            img = "repl_75";
        else if (perc >= 50)
            img = "repl_50";
        else if (perc >= 25)
            img = "repl_25";
        else
            img = "repl_pending";
        profile_replication_set_status(siteid, img, progress_text);
        setTimeout("profile_replication_step('"+siteid+"',"+est+", '"+progress_text+"');", est/20);
    }
}

function set_profile_replication_result(site_id, success, msg) {
    profile_replication_progress[site_id] = 0;

    var icon_name = success ? "repl_success" : "repl_failed";

    profile_replication_set_status(site_id, icon_name, msg);

    // g_num_replsites is set by the page code in wato.py to the number async jobs started
    // in total
    g_num_replsites--;

    if (0 == g_num_replsites) {
        setTimeout(wato_profile_replication_finish, 1000);
    }
}

function wato_profile_replication_finish() {
    // check if we have a sidebar-main frame setup
    if (this.parent && parent && parent.frames[1] == this)
        cmk.utils.reload_sidebar();
}

// ----------------------------------------------------------------------------
// Folderlist
// ----------------------------------------------------------------------------

function wato_open_folder(event, link) {
    if (!event)
        event = window.event;
    var target = getTarget(event);
    if(target.tagName != "DIV") {
        // Skip this event on clicks on other elements than the pure div
        return false;
    }

    location.href = link;
}

function wato_toggle_folder(event, oDiv, on) {
    if (!event)
        event = window.event;

    // Skip mouseout event when moving mouse over a child element of the
    // folder element
    if (!on) {
        var node = event.toElement || event.relatedTarget;
        while (node) {
            if (node == oDiv) {
                return false;
            }
            node = node.parentNode;
        }
    }

    var obj = oDiv.parentNode;
    var id = obj.id.substr(7);

    var elements = ["edit", "popup_trigger_move", "delete"];
    for(var num in elements) {
        var elem = document.getElementById(elements[num] + "_" + id);
        if(elem) {
            if(on) {
                elem.style.display = "inline";
            } else {
                elem.style.display = "none";
            }
        }
    }

    if(on) {
        add_class(obj, "open");
    } else {
        remove_class(obj, "open");

        // Hide the eventual open move dialog
        var move_dialog = document.getElementById("move_dialog_" + id);
        if(move_dialog) {
            move_dialog.style.display = "none";
        }
    }
}

// .--Host Diag-----------------------------------------------------------.
// |              _   _           _     ____  _                           |
// |             | | | | ___  ___| |_  |  _ \(_) __ _  __ _               |
// |             | |_| |/ _ \/ __| __| | | | | |/ _` |/ _` |              |
// |             |  _  | (_) \__ \ |_  | |_| | | (_| | (_| |              |
// |             |_| |_|\___/|___/\__| |____/|_|\__,_|\__, |              |
// |                                                  |___/               |
// +----------------------------------------------------------------------+

function handle_host_diag_result(data, response_json) {
    var response = JSON.parse(response_json);

    var img   = document.getElementById(data.ident + "_img");
    var log   = document.getElementById(data.ident + "_log");
    var retry = document.getElementById(data.ident + "_retry");
    remove_class(img, "reloading");

    var text = "";
    if (response.result_code == 1) {
        img.src = "images/icon_failed.png";
        log.className = "log diag_failed";
        text = "API Error:" + response.result;

    } else {
        if (response.result.status_code == 1) {
            img.src = "images/icon_failed.png";
            log.className = "log diag_failed";
        } else {
            img.src = "images/icon_success.png";
            log.className = "log diag_success";
        }
        text = response.result.output;
    }

    log.innerText = text;

    retry.src = "images/icon_reload.png";
    retry.style.display = "inline";
    retry.parentNode.href = "javascript:start_host_diag_test('"+data.ident+"', '"+data.hostname+"', '"+response.result.next_transid+"');";
}

function start_host_diag_test(ident, hostname, transid) {
    var log   = document.getElementById(ident + "_log");
    var img   = document.getElementById(ident + "_img");
    var retry = document.getElementById(ident + "_retry");

    retry.style.display = "none";

    var vars = "";
    vars = "&_transid=" + encodeURIComponent(transid);
    vars += "&ipaddress=" + encodeURIComponent(document.getElementsByName("vs_host_p_ipaddress")[0].value);


    if (document.getElementsByName("vs_host_p_snmp_community_USE")[0].checked)
        vars += "&snmp_community=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_community")[0].value);

    if (document.getElementsByName("vs_host_p_snmp_v3_credentials_USE")[0].checked) {
        v3_use = encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_use")[0].value);
        vars += "&snmpv3_use=" + v3_use;
        if (v3_use == "0") {
            vars += "&snmpv3_security_name=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_0_1")[0].value);
        }
        else if (v3_use == "1") {
            vars += "&snmpv3_auth_proto=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_1_1")[0].value);
            vars += "&snmpv3_security_name=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_1_2")[0].value);
            vars += "&snmpv3_security_password=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_1_3")[0].value);
        }
        else if (v3_use == "2") {
            vars += "&snmpv3_auth_proto=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_2_1")[0].value);
            vars += "&snmpv3_security_name=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_2_2")[0].value);
            vars += "&snmpv3_security_password=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_2_3")[0].value);
            vars += "&snmpv3_privacy_proto=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_2_4")[0].value);
            vars += "&snmpv3_privacy_password=" + encodeURIComponent(document.getElementsByName("vs_host_p_snmp_v3_credentials_2_5")[0].value);
        }
    }

    vars += "&agent_port=" + encodeURIComponent(document.getElementsByName("vs_rules_p_agent_port")[0].value);
    vars += "&tcp_connect_timeout=" + encodeURIComponent(document.getElementsByName("vs_rules_p_tcp_connect_timeout")[0].value);
    vars += "&snmp_timeout=" + encodeURIComponent(document.getElementsByName("vs_rules_p_snmp_timeout")[0].value);
    vars += "&snmp_retries=" + encodeURIComponent(document.getElementsByName("vs_rules_p_snmp_retries")[0].value);
    if (document.getElementsByName("vs_rules_p_datasource_program").length > 0) {
        vars += "&datasource_program=" + encodeURIComponent(document.getElementsByName("vs_rules_p_datasource_program")[0].value);
    }

    img.src = "images/icon_reload.png";
    add_class(img, "reloading");

    log.innerHTML = "...";
    get_url("wato_ajax_diag_host.py?host=" + encodeURIComponent(hostname)
        + "&_test=" + encodeURIComponent(ident) + vars,
        handle_host_diag_result, { "hostname": hostname, "ident": ident }); // eslint-disable-line indent
}

//#.
//#   .-Discovery----------------------------------------------------------.
//#   |              ____  _                                               |
//#   |             |  _ \(_)___  ___ _____   _____ _ __ _   _             |
//#   |             | | | | / __|/ __/ _ \ \ / / _ \ '__| | | |            |
//#   |             | |_| | \__ \ (_| (_) \ V /  __/ |  | |_| |            |
//#   |             |____/|_|___/\___\___/ \_/ \___|_|   \__, |            |
//#   |                                                  |___/             |
//#   +--------------------------------------------------------------------+
//#   | Handling of the asynchronous service discovery dialog              |
//#   '--------------------------------------------------------------------'

// Stores the latest discovery_result object which was used by the python
// code to render the current page. It will be sent back to the python
// code for further actions. It contains the check_table which actions of
// the user are based on.
var g_service_discovery_result = null;
var g_show_updating_timer = null;

function start_service_discovery(host_name, folder_path, discovery_options, transid, request_vars)
{
    // When we receive no response for 2 seconds, then show the updating message
    g_show_updating_timer = setTimeout(function() {
        cmk.async_progress.show_info("Updating...");
    }, 2000);

    lock_service_discovery_controls(true);
    cmk.async_progress.monitor({
        "update_url" : "ajax_service_discovery.py",
        "host_name": host_name,
        "folder_path": folder_path,
        "transid": transid,
        "start_time" : cmk.utils.time(),
        "is_finished_function": is_service_discovery_finished,
        "update_function": update_service_discovery,
        "finish_function": finish_service_discovery,
        "post_data": get_service_discovery_post_data(host_name, folder_path, discovery_options, transid, request_vars)
    });
}

function get_service_discovery_post_data(host_name, folder_path, discovery_options, transid, request_vars)
{
    var request = {
        "host_name": host_name,
        "folder_path": folder_path,
        "discovery_options": discovery_options,
        "discovery_result": g_service_discovery_result
    };

    if (request_vars !== undefined && request_vars !== null) {
        request = Object.assign(request, request_vars);
    }

    if (discovery_options.action == "bulk_update") {
        var checked_checkboxes = [];
        var checkboxes = document.getElementsByClassName("service_checkbox");
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                checked_checkboxes.push(checkboxes[i].name);
            }
        }
        request["update_services"] = checked_checkboxes;
    }

    var post_data = "request=" + encodeURIComponent(JSON.stringify(request));

    // Can currently not be put into "request" because the generic transaction
    // manager relies on the HTTP var _transid.
    if (transid !== undefined)
        post_data += "&_transid=" + encodeURIComponent(transid);

    return post_data;
}

function is_service_discovery_finished(response) {
    return response.is_finished;
}

function finish_service_discovery(response)
{
    if (response.job_state == "exception"
        || response.job_state == "stopped") {
        cmk.async_progress.show_error(response.message);
    } else {
        //cmk.async_progress.hide_msg();
    }
    lock_service_discovery_controls(false);
}

function update_service_discovery(handler_data, response) {
    if (g_show_updating_timer) {
        clearTimeout(g_show_updating_timer);
    }

    if (response.message) {
        cmk.async_progress.show_info(response.message);
    } else {
        cmk.async_progress.hide_msg();
    }

    g_service_discovery_result = response.discovery_result;
    handler_data.post_data = get_service_discovery_post_data(handler_data.host_name, handler_data.folder_path, response.discovery_options, handler_data.transid);

    var container = document.getElementById("service_container");
    container.style.display = "block";
    container.innerHTML = response.body;
    executeJSbyObject(container);

    update_service_discovery_activate_changes_button(response);
}

function update_service_discovery_activate_changes_button(response)
{
    var tmp_container = document.createElement("div");
    tmp_container.innerHTML = response.changes_button;
    var context_buttons_container = document.getElementsByClassName("contextlinks")[0];
    var cur_changes_button = context_buttons_container.childNodes[0];
    context_buttons_container.replaceChild(tmp_container.childNodes[0].childNodes[0], cur_changes_button);
}

function lock_service_discovery_controls(lock)
{
    var elements = [];
    //elements.push(document.getElementById("activate_affected"));
    //elements.push(document.getElementById("activate_selected"));
    //// TODO: Remove once new changes mechanism has been implemented
    //elements.push(document.getElementById("discard_changes_button"));

    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("service_checkbox"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("button"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("service_button"), 0));

    for (var i = 0; i < elements.length; i++) {
        if (!elements[i])
            continue;

        if (lock)
            add_class(elements[i], "disabled");
        else
            remove_class(elements[i], "disabled");

        elements[i].disabled = lock;
    }
}


// .-Active Checks---------------------------------------------------------.
// |       _        _   _              ____ _               _              |
// |      / \   ___| |_(_)_   _____   / ___| |__   ___  ___| | _____       |
// |     / _ \ / __| __| \ \ / / _ \ | |   | '_ \ / _ \/ __| |/ / __|      |
// |    / ___ \ (__| |_| |\ V /  __/ | |___| | | |  __/ (__|   <\__ \      |
// |   /_/   \_\___|\__|_| \_/ \___|  \____|_| |_|\___|\___|_|\_\___/      |
// |                                                                       |
// '-----------------------------------------------------------------------'

function execute_active_check(site, folder_path, hostname, checktype, item, divid)
{
    var oDiv = document.getElementById(divid);
    var url = "wato_ajax_execute_check.py?" +
           "site="       + encodeURIComponent(site) +
           "&folder="    + encodeURIComponent(folder_path) +
           "&host="      + encodeURIComponent(hostname)  +
           "&checktype=" + encodeURIComponent(checktype) +
           "&item="      + encodeURIComponent(item);
    get_url(url, handle_execute_active_check, oDiv);
}


function handle_execute_active_check(oDiv, response_json)
{
    var response = JSON.parse(response_json);

    var state, statename, output;
    if (response.result_code == 1) {
        state = 3;
        statename = "UNKN";
        output = response.result;
    } else {
        state = response.result.state;
        if (state == -1)
            state = "p"; // Pending
        statename = response.result.state_name;
        output    = response.result.output;
    }

    oDiv.innerHTML = output;

    // Change name and class of status columns
    var oTr = oDiv.parentNode.parentNode;
    if (has_class(oTr, "even0"))
        add_class(oTr, "even" + state);
    else
        add_class(oTr, "odd" + state);

    var oTdState = oTr.getElementsByClassName("state")[0];
    remove_class(oTdState, "statep");
    add_class(oTdState, "state" + state);

    oTdState.innerHTML = statename;
}
