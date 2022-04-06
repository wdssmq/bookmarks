// Docsify plugin functions
function footmarks_count(hook, vm) {
  console.log(vm);
  hook.beforeEach(function (content) {
    if (!vm.route.file.startsWith('footmarks/')) {
      return content;
    }
    vm.config.autoHeader = false;
    // 换行符统一
    content = content.replace(/\r/g, '').replace(/\n+$/, '');
    // js count \n in string
    const itemsCount = content.trim().split("\n\n").length - 1;
    content = content.replace(/\n\n/, ` - 「${itemsCount}」\n\n`);
    return content;
  });
}

// Docsify plugin
window.$docsify.plugins = [].concat(footmarks_count, window.$docsify.plugins);
