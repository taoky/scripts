#!/usr/bin/env python3
# img_convert.py – super-simple image converter for Nautilus

import os

from gi.repository import Nautilus, GObject, Gio, GLib

ALLOWED = {"jpg", "png", "webp", "heic"}


_running = set()  # avoid proc being gc

def spawn_nonblocking(argv):
    proc = Gio.Subprocess.new(argv, Gio.SubprocessFlags.NONE)
    _running.add(proc)

    def on_done(proc, res, data=None):
        try:
            ok = proc.wait_check_finish(res)
        except GLib.Error as e:
            pass
        finally:
            _running.discard(proc)

    proc.wait_check_async(None, on_done)


class ImgConvertExtension(GObject.GObject, Nautilus.MenuProvider):
    """Adds  Convert to → JPG / PNG / WEBP  items to Nautilus context menu."""

    # ——菜单——
    def get_file_items(self, files: list[Nautilus.FileInfo]):
        paths, src_exts = [], set()

        for f in files:
            # 仅处理本地普通文件
            if f.get_uri_scheme() != "file" or f.is_directory():
                return
            path = f.get_location().get_path()
            ext = os.path.splitext(path)[1].lstrip(".").lower()
            if ext not in ALLOWED:  # 若有一个不在列表里就不显示菜单
                return
            paths.append(path)
            src_exts.add(ext)

        targets = sorted(ALLOWED - src_exts)  # 不把“自己”列出来
        if not targets:
            return

        top_item = Nautilus.MenuItem(
            name="ImgConvert::Top", label="Convert to", icon="image-x-generic"
        )
        submenu = Nautilus.Menu()
        top_item.set_submenu(submenu)

        for fmt in targets:  # 加入可转格式
            sub = Nautilus.MenuItem(
                name=f"ImgConvert::{fmt}", label=fmt.upper(), icon="image-x-generic"
            )
            sub.connect("activate", self.convert, paths, fmt)
            submenu.append_item(sub)

        return [top_item]

    # ——回调——
    def convert(self, _menu, files, fmt):
        for src in files:
            base, _ = os.path.splitext(src)
            dst = f"{base}.{fmt}"
            spawn_nonblocking(["magick", src, dst])
