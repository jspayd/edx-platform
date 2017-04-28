(function() {
    'use strict';
    var Metrics;

    Metrics = (function() {
        function metrics($section) {
            this.$section = $section;
            this.$section.data('wrapper', this);
        }

        metrics.prototype.onClickTitle = function() {
            loadGraphs();
            $('#graph_reload').show();
            $('.metrics-header-container').show();
        };

        return metrics;
    }());

    window.InstructorDashboard.sections.Metrics = Metrics;
}).call(this);
