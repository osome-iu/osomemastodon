import Swal from 'sweetalert2'

export function showErrorMessage(message) {
    Swal.fire({
        title: 'Error',
        text: message,
        icon: 'warning',
    }).then(
        function() {},
        function(dismiss) {
            if (dismiss === 'timer') {
            }
        }
    );
}
