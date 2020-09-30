# Using Puppet, to fix wordpress file extension mistake
exec {'fix-wordpress':
  path    => '/bin/',
  command => 'sed -i s/.phpp/.php/ /var/www/html/wp-settings.php',
}
