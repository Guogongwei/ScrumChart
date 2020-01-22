class Scrum{
    constructor() {
        this.initEvent();
    }

    initEvent() {
        $('.update-scrum').on('click', (event) => this.updateScrum(event));
        $('.point-input').on('blur', (event) => this.updatePost(event));
    }

    updateScrum(event) {
        let $target = $(event.currentTarget);
        let $pointItem = $target.closest('tr').find('.point-item');
        let $inputItem = $target.closest('tr').find('.point-input');
        if ($inputItem.hasClass('hidden')) {
            $pointItem.addClass('hidden');
            $inputItem.removeClass('hidden');
        }
    }

    updatePost(event) {
        let $target = $(event.currentTarget);
        console.log($target.data('id'));
        let data = {
            scrum_id: $target.data('id'),
            sprint_id: $target.closest('tr').find('.item-id').text(),
            left_sprint: $target.val(),
        };
        console.log($target.data('url'));
        $.post($target.data('url'), data, function (result) {
            if (result == 'true') {
                window.location.reload();
            }
        });
    }
}

new Scrum();