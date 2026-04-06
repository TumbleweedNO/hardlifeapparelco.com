<?php
/**
 * Plugin Name: HRDLF Follow Button Fix
 * Description: Fixes the FOLLOW button in the footer to link to Hardwired Weekly on Beehiiv instead of WP.com Reader subscribe.
 * Version: 1.0.0
 * Author: HRDLF
 */

add_action( 'wp_footer', function() {
    ?>
    <script>
    (function(){
        var btn = document.querySelector('.hrdlf-wp-follow-btn');
        if (btn) {
            btn.href = 'https://hardwiredweekly.beehiiv.com/subscribe';
        }
    })();
    </script>
    <?php
}, 999 );
