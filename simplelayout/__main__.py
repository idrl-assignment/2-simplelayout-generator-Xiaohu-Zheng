# TODO 正确导入函数 generate_matrix, save_matrix, save_fig
from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入
import untils
import core


def main():
    options = get_options()
    untils.make_dir(options.outdir)
    matrix = core.generate_matrix(options.board_grid)
    save_matrix(matrix, options.outdir + '/' + options.file_name)
    save_fig(matrix, options.outdir + '/' + options.file_name)


if __name__ == "__main__":
    main()
