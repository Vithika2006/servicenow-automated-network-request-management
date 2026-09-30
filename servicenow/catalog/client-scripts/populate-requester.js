/**
 * Minimal design for requester context population.
 *
 * Prefer ServiceNow-supported variable auto-population/reference mechanisms
 * in the target release. If scripting is required, use a scoped Script Include
 * with GlideAjax and return only the required user fields.
 */
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading || typeof g_form === 'undefined') {
        return;
    }

    var source = 'opened_on_behalf_of';
    if (!g_form.getValue(source)) {
        g_form.clearValue('email_id');
        g_form.clearValue('user_name');
        g_form.clearValue('phone_number');
    }

    // Intentionally no hard-coded sys_id/user lookup.
    // Configure platform-supported auto-population in the PDI first.
}
