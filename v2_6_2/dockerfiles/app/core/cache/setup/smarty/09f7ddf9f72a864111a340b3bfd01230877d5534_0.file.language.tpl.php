<?php
/* Smarty version 3.1.31, created on 2019-05-28 13:16:43
  from "/var/www/html/modx-2.6.2-pl/setup/templates/language.tpl" */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.31',
  'unifunc' => 'content_5ced34bb0f8253_57646934',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '09f7ddf9f72a864111a340b3bfd01230877d5534' => 
    array (
      0 => '/var/www/html/modx-2.6.2-pl/setup/templates/language.tpl',
      1 => 1522336048,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5ced34bb0f8253_57646934 (Smarty_Internal_Template $_smarty_tpl) {
?>
<form id="install" action="?" method="post">

<?php if ($_smarty_tpl->tpl_vars['restarted']->value) {?>
    <br class="clear" />
    <br class="clear" />
    <p class="note"><?php echo $_smarty_tpl->tpl_vars['_lang']->value['restarted_msg'];?>
</p>
<?php }?>

<div class="setup_navbar" style="border-top: 0;">
    <p class="title"><?php echo $_smarty_tpl->tpl_vars['_lang']->value['choose_language'];?>
:
        <select name="language" autofocus="autofocus">
            <?php echo $_smarty_tpl->tpl_vars['languages']->value;?>

    	</select>
    </p>

    <input type="submit" name="proceed" value="<?php echo $_smarty_tpl->tpl_vars['_lang']->value['select'];?>
" />
</div>
</form><?php }
}
